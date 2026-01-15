import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/axios";
import "../styles/enterprise.css";

/* ================= TYPES ================= */

interface Project {
  id: number;
  title: string;
  description: string;
  status: "draft" | "active" | "completed";
}

interface Member {
  user_id: number;
  role: "talent" | "mentor";
  status: "pending" | "approved" | "rejected";
}

/* ================= COMPONENT ================= */

export default function EnterpriseDashboard() {
  const navigate = useNavigate();

  const [projects, setProjects] = useState<Project[]>([]);
  const [members, setMembers] = useState<Member[]>([]);
  const [selectedProjectId, setSelectedProjectId] = useState<number | null>(null);
  const [loading, setLoading] = useState<boolean>(false);

  /* ================= FETCH PROJECTS ================= */

  useEffect(() => {
    setLoading(true);
    api
      .get("/projects/my-projects")
      .then(res => setProjects(res.data || []))
      .catch(err => console.error("Failed to load projects", err))
      .finally(() => setLoading(false));
  }, []);

  /* ================= OPEN APPLICANTS ================= */

  const openApplicants = (projectId: number) => {
    setSelectedProjectId(projectId);
    setLoading(true);

    api
      .get(`/projects/${projectId}/members`)
      .then(res => setMembers(res.data || []))
      .catch(err => console.error("Failed to load members", err))
      .finally(() => setLoading(false));
  };

  const closeModal = () => {
    setSelectedProjectId(null);
    setMembers([]);
  };

  /* ================= ACTIONS ================= */

  const approveMember = (userId: number) => {
    // mock API – bạn có thể nối backend sau
    setMembers(prev =>
      prev.map(m =>
        m.user_id === userId ? { ...m, status: "approved" } : m
      )
    );
  };

  const rejectMember = (userId: number) => {
    setMembers(prev =>
      prev.map(m =>
        m.user_id === userId ? { ...m, status: "rejected" } : m
      )
    );
  };

  /* ================= RENDER ================= */

  return (
    <div className="enterprise-layout">
      <h1 className="page-title">📁 My Projects</h1>

      <button
        className="btn-primary new-project-btn"
        onClick={() => navigate("/enterprise/projects/create")}
      >
        ➕ New Project
      </button>

      {loading && <p>Loading...</p>}

      <div className="project-grid">
        {projects.map(project => (
          <div className="project-card" key={project.id}>
            <div className="card-header">
              <h3>{project.title}</h3>
              <span className={`badge ${project.status}`}>
                {project.status.toUpperCase()}
              </span>
            </div>

            <p className="desc">{project.description}</p>

            <div className="card-footer">
              <span>ID #{project.id}</span>
              <button
className="btn-view"
                onClick={() => openApplicants(project.id)}
              >
                View Applicants
              </button>
            </div>
          </div>
        ))}
      </div>

      {/* ================= MODAL ================= */}

      {selectedProjectId !== null && (
        <div className="modal-backdrop" onClick={closeModal}>
          <div className="modal" onClick={e => e.stopPropagation()}>
            <h2>👥 Applicants</h2>

            <table className="member-table">
              <thead>
                <tr>
                  <th>User ID</th>
                  <th>Role</th>
                  <th>Status</th>
                  <th>Action</th>
                </tr>
              </thead>

              <tbody>
                {members.length === 0 && (
                  <tr>
                    <td colSpan={4}>No applicants</td>
                  </tr>
                )}

                {members.map(member => (
                  <tr key={member.user_id}>
                    <td>#{member.user_id}</td>
                    <td>{member.role.toUpperCase()}</td>
                    <td>
                      <span className={`status ${member.status}`}>
                        {member.status.toUpperCase()}
                      </span>
                    </td>
                    <td>
                      {member.status === "pending" && (
                        <>
                          <button
                            className="btn-approve"
                            onClick={() => approveMember(member.user_id)}
                          >
                            Approve
                          </button>
                          <button
                            className="btn-reject"
                            onClick={() => rejectMember(member.user_id)}
                          >
                            Reject
                          </button>
                        </>
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>

            <button className="btn-close" onClick={closeModal}>
              Close
            </button>
          </div>
        </div>
      )}
    </div>
  );
}