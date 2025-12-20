from dependency_container import init_application_db


def main():
    # Initialize database tables
    init_application_db()
    print("Database initialized. Add web server wiring (Flask/FastAPI) as needed.")


if __name__ == '__main__':
    main()
