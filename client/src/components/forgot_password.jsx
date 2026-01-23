import { useState } from 'react';
import { Link } from 'react-router-dom';
import './Login.css';
import './forgot_password.css';

export default function ForgotPassword() {
    const [email, setEmail] = useState('');
    const [submitted, setSubmitted] = useState(false);
    const [error, setError] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        setError('');
        const validEmail = ['systemadmin@gmail.com','labadmin@gmail.com','mentor@gmail.com','candidate@gmail.com','enterprise@gmail.com'];
    if (!validEmail.includes(email)) {
      setError('Email address does not exist!');
      return;
    }
    setSubmitted(true);
    };
    if (submitted) {
        return (
        <div className="login-container">
            <div className="login-card">
                <div className="login-header">
                    <p className="login-subtitle">
                        Please check your email
                    </p>
                </div>
                <Link to="/login" className="back-to-login">
                Back to login
                </Link>
            </div>
        </div>
        );
    }

    return (
    <div className="login-container">
      <div className="login-card">
        <div className="login-header-lp">
          <h1 className="login-title">Forgot password?</h1>
          <p className="login-subtitle">
            please enter your email
          </p>
        </div>
        {error && <div className="error-message">{error}</div>}
        <form onSubmit={handleSubmit} className="login-form">
          <div className="form-group-fp">
            <div className="input-wrapper-fp">
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
        </form>

        <div className="login-footer">
          <Link to="/login" className="back-link">
            back to login
          </Link>
        </div>
      </div>
    </div>
  );
}