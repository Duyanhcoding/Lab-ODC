import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../auth/AuthContext'; // Sử dụng context đã tạo 
import '../styles/login.css';
import '../styles/forgot_password.css';

export default function ForgotPassword() {
  const [email, setEmail] = useState('');
  const [submitted, setSubmitted] = useState(false);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  
  // Lấy hàm forgotPassword từ context 
  const { forgotPassword } = useAuth();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      setError('Invalid email');
      return;
    }

    setLoading(true);
    try {
      await forgotPassword(email);
      setSubmitted(true); 
    } catch (err: any) {
      console.error('Forgot password error:', err);
      let errorMessage = 'invalid input, please try again';
      
      if (err.response?.data?.detail) {
        errorMessage = err.response.data.detail; 
      } else if (err.response?.data?.message) {
        errorMessage = err.response.data.message; 
      } else if (err.response?.status === 404) {
        errorMessage = 'Email does not exists'; 
      }
      setError(errorMessage);
    } finally {
      setLoading(false); 
    }
  };

  if (submitted) {
    return (
      <div className="login-container">
        <div className="login-card">
          <div className="login-header">
            <h1 className="login-title">✓ email has been sent</h1>
            <p className="login-subtitle">
              please check your email
            </p>
          </div>
          <Link to="/login" className="submit-login" style={{ textAlign: 'center', display: 'block', marginTop: '20px', textDecoration: 'none' }}>
            Back to login
          </Link> 
        </div>
      </div>
    );
  }

  return (
    <div className="login-container">
      <div className="login-card">
        <div className="login-header">
          <h1 className="login-title">Forgot password?</h1>
          <p className="login-subtitle">
            enter your email
          </p>
        </div>

        {error && <div className="error-message" style={{ color: 'red', marginBottom: '10px' }}>{error}</div>}

        <form onSubmit={handleSubmit} className="login-form"> 
          <div className="form-group">
            <div className="input-wrapper">
              <input
                type="email"
                id="email"
                value={email} 
                onChange={(e) => setEmail(e.target.value)} 
                className="form-input"
                placeholder="email"
                required
              />
            </div>
          </div>

          <button 
            className="submit-login" 
            type="submit"
            disabled={loading}
          >
            {loading ? 'Processing...' : 'submit request'} 
          </button>
        </form>

        <div className="options" style={{ marginTop: '20px' }}>
          <Link to="/login" className="forgot-link">
            ← Back to login
          </Link>
        </div>
      </div>
    </div>
  );
}