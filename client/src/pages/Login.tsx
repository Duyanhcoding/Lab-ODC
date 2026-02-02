import React, { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { Eye, EyeOff } from 'lucide-react';
import { useAuth } from "../auth/AuthContext";
import "../styles/login.css";
import "../styles/theme.css";

export default function Login() {
  const [isLogin, setIsLogin] = useState(true);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [fullName, setFullName] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [role, setRole] = useState("talent");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const { login, register } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");

    if (!isLogin) {
      // Kiểm tra đầy đủ thông tin
      if (!fullName.trim()) {
        setError("please enter your full name");
        return;
      }

      // Kiểm tra email hợp lệ
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(email)) {
        setError("Invalid Email");
        return;
      }

      // Kiểm tra độ dài mật khẩu
      if (password.length < 8) {
        setError("password must be at least 6 characters long");
        return;
      }
    }

    setLoading(true);

    try {
      if (isLogin) {
        await login(email, password);
      } else {
        console.log("Registering with data:", {
          email: email,
          password: password,
          full_name: fullName,
          role: role
        });
        
        await register({
          email: email,
          password: password,
          full_name: fullName,
          role: role
        });
      }

      // Lấy user từ localStorage 
      const u = JSON.parse(localStorage.getItem("user")!);

      // chuyển hướng theo role
      if (u.role === "admin") {
        navigate("/admin/dashboard");
      } else if (u.role === "enterprise") {
        navigate("/enterprise/dashboard");
      } else if (u.role === "mentor") {
        navigate("/mentor/dashboard");
      } else {
        navigate("/talent/dashboard");
      }
    } catch (err: any) {
      console.error("Full error:", err);
      console.error("Error response:", err.response);
      
      // Hiển thị error message chi tiết hơn
      let errorMessage = "Authentication failed";
      
      if (err.response?.data?.detail) {
        errorMessage = err.response.data.detail;
      } else if (err.response?.data?.message) {
        errorMessage = err.response.data.message;
      } else if (err.message) {
        errorMessage = err.message;
      }
      
      setError(errorMessage);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="login-container">
      <div className="login-card">
        <h1>{isLogin ? "LabODC" : "LabODC"}</h1>

        {error && <div className="error-message">{error}</div>}

        <form onSubmit={handleSubmit} className="login-form">
          
          {/* Full Name - chỉ hiện khi Register */}
          {!isLogin && (
            <div className="form">
              <div className="input-wrapper">
                <input
                  type="text"
                  placeholder="Full Name"
                  value={fullName}
                  onChange={(e) => setFullName(e.target.value)}
                  required
                  className="form-input"
                />
              </div>
            </div>
          )}

          <div className="form">
            <div className="input-wrapper">
              <input
                type="email"
                placeholder="Email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
                className="form-input"
              />
            </div>
          </div>

          <div className="form">
            <div className="input-wrapper">
              <input
                type={showPassword ? 'text' : 'password'}
                id="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
                className="form-input"
              />
              <button
                type="button"
                onClick={() => setShowPassword(!showPassword)}
                className="show"
              >
                {showPassword ? <EyeOff className="icon"/> : <Eye className="icon"/>}
              </button>
            </div>
          </div>
        
          {!isLogin && (
            <>
              <select value={role} onChange={(e) => setRole(e.target.value)}>
                <option value="talent">Talent</option>
                <option value="mentor">Mentor</option>
                <option value="enterprise">Enterprise</option>
                <option value="admin">Admin</option>
              </select>
            </>
          )}

          <button 
            className="submit-login" 
            type="submit"
            disabled={loading}
          >
            {loading ? "Processing..." : (isLogin ? "Login" : "Register")}
          </button>
        </form>

        <p className="toggle-auth">
          {isLogin ? "Don't have an account? " : "Already have an account? "}
          <span onClick={() => setIsLogin(!isLogin)}>
            {isLogin ? "Register" : "Login"}
          </span>
        </p>
        <div className="options">
          <Link to="/forgot-password" className="forgot-link">
            Forgot password?
          </Link>
        </div>
      </div>
    </div>
  );
}
