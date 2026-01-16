import { Outlet, useNavigate, useLocation } from "react-router-dom";
import "../styles/enterprise.css";

export default function EnterpriseLayout() {
  const navigate = useNavigate();
  const location = useLocation();

  /**
   * Determine active menu item based on current path
   */
  const isActive = (path: string) => {
    return location.pathname.startsWith(path) ? "active" : "";
  };

  return (
    <div className="enterprise-shell">
      {/* ===== SIDEBAR ===== */}
      <aside className="enterprise-sidebar">
        <div className="logo">LabOdc</div>

        <nav>
          <div
            className={`nav-item ${isActive("/enterprise/dashboard")}`}
            onClick={() => navigate("/enterprise/dashboard")}
          >
            📁 Projects
          </div>

          <div
            className={`nav-item ${isActive("/enterprise/payments")}`}
            onClick={() => navigate("/enterprise/payments")}
          >
            💳 Payments
          </div>

          <div
            className={`nav-item ${isActive("/enterprise/profile")}`}
            onClick={() => navigate("/enterprise/profile")}
          >
            👤 Profile
          </div>
        </nav>
      </aside>

      {/* ===== MAIN CONTENT (ROUTE OUTLET) ===== */}
      <main className="enterprise-main">
        <Outlet />
      </main>
    </div>
  );
}
