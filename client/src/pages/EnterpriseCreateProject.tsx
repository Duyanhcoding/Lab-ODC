import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/axios";
import "../styles/enterprise.css";

export default function EnterpriseCreateProject() {
  const navigate = useNavigate();

  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [loading, setLoading] = useState(false);

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (loading) return;

    setLoading(true);

    try {
      await api.post("/projects", {
        title,
        description,
        status: "draft"
      });

      // reset form
      setTitle("");
      setDescription("");

      // quay về danh sách project enterprise
      navigate("/enterprise/projects");
    } catch (error) {
      console.error("Create project error:", error);
      alert("❌ Failed to create project. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="enterprise-layout">
      <h1 className="page-title">➕ Create New Project</h1>

      <form className="project-form" onSubmit={submit}>
        <label>
          Project Title
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="e.g. AI Resume Screening System"
            required
          />
        </label>

        <label>
          Project Description
          <textarea
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            placeholder="Describe objectives, scope, expected outcomes..."
            required
          />
        </label>

        <button
          className="btn-primary"
          type="submit"
          disabled={loading}
        >
          {loading ? "Creating project..." : "Create Project"}
        </button>
      </form>
    </div>
  );
}
