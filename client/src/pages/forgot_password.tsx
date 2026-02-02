import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import api from '../api/axios';
import '../styles/login.css';
import '../styles/forgot_password.css';

export default function ForgotPassword() {
  const [email, setEmail] = useState('');
  const [submitted, setSubmitted] = useState(false);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setError('');
    
    // Validation email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      setError('Invalid email');
      return;
    }

    setLoading(true);

    try {
      // Gọi API forgot password
      const response = await api.post('/auth/forgot-password', { email });
      
      console.log('Forgot password response:', response.data);
      
      // Nếu thành công
      setSubmitted(true);
    } catch (err: any) {
      console.error('Forgot password error:', err);
      
      // Xử lý error message
      let errorMessage = 'An error occurred. please try again';
      
      if (err.response?.data?.detail) {
        errorMessage = err.response.data.detail;
      } else if (err.response?.data?.message) {
        errorMessage = err.response.data.message;
      } else if (err.response?.status === 404) {
        errorMessage = 'This email address is not registered';
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
            <h1 className="login-title">✓ Email has been sent</h1>
            <p className="login-subtitle">
              please enter your email
            </p>
          </div>
          <Link to="/login" className="submit-login" style={{ textAlign: 'center', display: 'block', marginTop: '20px' }}>
            Back to login
          </Link>
        </div>
      </div>
    );
  }

  // Form nhập email
  return (
    <div className="login-container">
      <div className="login-card">
        <div className="login-header">
          <h1 className="login-title">Forgot password?</h1>
          <p className="login-subtitle">
            enter your email
          </p>
        </div>

        {error && <div className="error-message">{error}</div>}

        <form onSubmit={handleSubmit} className="login-form">
          <div className="form-group">
            <div className="input-wrapper">
              <input
                type="email"
                id="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="form-input"
                placeholder="Email"
                required
              />
            </div>
          </div>

          <button 
            className="submit-login" 
            type="submit"
            disabled={loading}
          >
            {loading ? 'Processing...' : 'send email'}
          </button>
        </form>

        <div className="options" style={{ marginTop: '20px' }}>
          <Link to="/login" className="forgot-link">
            Back to login
          </Link>
        </div>
      </div>
    </div>
  );
}
