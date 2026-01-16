import { useEffect, useState } from "react";
import api from "../api/axios";
import "../styles/enterprise.css";

/* ================= TYPES ================= */
interface Payment {
  id: string;
  project_title: string;
  amount: number;
  status: "paid" | "pending";
  fund_talent?: number;
  fund_mentor?: number;
  fund_platform?: number;
}

/* ================= COMPONENT ================= */
export default function EnterprisePayments() {
  const [payments, setPayments] = useState<Payment[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api
      .get("/payments/enterprise")
      .then((res) => setPayments(res.data || []))
      .catch((err) => console.error("Payment API error:", err))
      .finally(() => setLoading(false));
  }, []);

  /* ===== STATS ===== */
  const totalPaid = payments
    .filter((p) => p.status === "paid")
    .reduce((sum, p) => sum + p.amount, 0);

  const pendingCount = payments.filter(
    (p) => p.status === "pending"
  ).length;

  return (
    <div className="enterprise-layout">
      {/* ===== HEADER ===== */}
      <header className="ent-header">
        <div>
          <h1>💳 Payments & Invoices</h1>
          <p>Track your project payments and fund distribution</p>
        </div>
      </header>

      {/* ===== STATS ===== */}
      <div className="ent-stats">
        <Stat title="Total Paid" value={`$${totalPaid}`} />
        <Stat title="Invoices" value={payments.length} />
        <Stat title="Pending" value={pendingCount} />
      </div>

      {/* ===== TABLE ===== */}
      <div className="payment-table">
        <div className="table-head">
          <span>Project</span>
          <span>Amount</span>
          <span>Status</span>
          <span>Invoice</span>
        </div>

        {/* LOADING */}
        {loading && <p>Loading payments...</p>}

        {/* EMPTY */}
        {!loading && payments.length === 0 && (
          <p>No payment records found.</p>
        )}

        {/* DATA */}
        {payments.map((p) => (
          <div className="table-row card" key={p.id}>
            {/* MAIN ROW */}
            <div className="row-main">
              <span className="title">{p.project_title}</span>
              <span className="amount">${p.amount}</span>

              <span className={`badge ${p.status}`}>
                {p.status.toUpperCase()}
              </span>

              <button className="btn-outline">
                ⬇ Download
              </button>
            </div>

            {/* FUND BAR (70/20/10) */}
            <div className="fund-bar">
              <div
                className="fund talent"
                style={{ width: "70%" }}
              />
              <div
                className="fund mentor"
                style={{ width: "20%" }}
              />
              <div
                className="fund platform"
                style={{ width: "10%" }}
              />
            </div>

            {/* FUND DETAILS */}
            <ul className="fund-list">
              <li>
                <span>
                  <span className="dot fund talent" /> Talent (70%)
                </span>
                <span>${p.fund_talent ?? p.amount * 0.7}</span>
              </li>
              <li>
                <span>
                  <span className="dot fund mentor" /> Mentor (20%)
                </span>
                <span>${p.fund_mentor ?? p.amount * 0.2}</span>
              </li>
              <li>
                <span>
                  <span className="dot fund platform" /> LabOdc (10%)
                </span>
                <span>${p.fund_platform ?? p.amount * 0.1}</span>
              </li>
            </ul>
          </div>
        ))}
      </div>
    </div>
  );
}

/* ================= STAT CARD ================= */
function Stat({ title, value }: { title: string; value: string | number }) {
  return (
    <div className="ent-stat-card">
      <p>{title}</p>
      <h3>{value}</h3>
    </div>
  );
}