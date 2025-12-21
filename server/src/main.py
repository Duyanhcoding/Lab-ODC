"""LabOdc: FastAPI application entrypoint (refactored as requested)

- Structure borrowed from your sample: logging, startup DB test, controllers.
- Does NOT modify `database.py` or `config.py` (per your request).
- Run from project root, e.g. `python -m server.src.main run`.
"""

import sys
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("labodc")

# Import DB test helper robustly using multiple strategies
import importlib

test_connection = None
# 1) Try relative import (works when running as `-m server.src.main`)
try:
    from .database import test_connection  # type: ignore
except Exception:
    # 2) Try importing with fully qualified package name
    try:
        db_mod = importlib.import_module("server.src.database")
        test_connection = getattr(db_mod, "test_connection", None)
    except Exception:
        # 3) Fallback to top-level import if present
        try:
            from database import test_connection  # type: ignore
        except Exception as e:
            logger.warning("Không import được test_connection: %s", e)
            test_connection = None

# Create FastAPI app
app = FastAPI(title="LabOdc API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def on_startup():
    logger.info("Starting LabOdc API...")
    if test_connection is not None:
        try:
            test_connection()
            logger.info("DB connection OK")
        except Exception as e:
            logger.exception("DB connection failed on startup: %s", e)
    else:
        logger.warning("test_connection not configured; skipping DB check")


# Import controllers with safe fallbacks (package-relative first)
auth_controller = None
user_controller = None
audit_log_controller = None
try:
    from .api.controllers import auth_controller, user_controller, audit_log_controller  # type: ignore
except Exception:
    try:
        from api.controllers import auth_controller, user_controller, audit_log_controller
    except Exception as e:
        logger.warning("Controllers import failed, some endpoints may be disabled: %s", e)
        auth_controller = None
        user_controller = None
        audit_log_controller = None

# Register routers (use package-relative imports so -m works)
try:
    from .api.routes import projects, reports, teams, funds  # type: ignore
except Exception:
    from api.routes import projects, reports, teams, funds

if user_controller is not None:
    app.include_router(user_controller.router)
else:
    try:
        from .api.routes import users as users_module  # type: ignore
    except Exception:
        from api.routes import users as users_module
    app.include_router(users_module.router)

if auth_controller is not None:
    app.include_router(auth_controller.router)

if audit_log_controller is not None:
    app.include_router(audit_log_controller.router)

app.include_router(projects.router)
app.include_router(reports.router)
app.include_router(teams.router)
app.include_router(funds.router)


@app.get("/")
def root():
    return {"message": "LabOdc API is running"}


@app.get("/api/health")
def health_check():
    db_status = "unknown"
    if test_connection is not None:
        try:
            test_connection()
            db_status = "connected"
        except Exception as e:
            db_status = f"error: {e}"
    else:
        db_status = "not configured"

    return {"status": "ok", "database": db_status, "service": "running"}


def _print_usage():
    print("Usage:")
    print("  python -m server.src.main run       # start server (from project root)")
    print("  python -m server.src.main init-db    # create DB tables")
    print("  python -m server.src.main test-conn  # check DB connection")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else None
    if cmd == "run":
        try:
            import uvicorn
        except Exception as e:
            logger.error("uvicorn not installed: %s", e)
            print("pip install uvicorn[standard]")
            sys.exit(1)
        uvicorn.run("server.src.main:app", host="127.0.0.1", port=8000, reload=True)
    elif cmd == "init-db":
        from dependency_container import init_application_db

        init_application_db()
        print("✅ Database initialized.")
    elif cmd == "test-conn":
        if test_connection is not None:
            test_connection()
        else:
            print("test_connection not configured")
    else:
        _print_usage()