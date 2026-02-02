import { useState,useEffect,useRef } from 'react';
import { Eye, EyeOff} from 'lucide-react';
import {useNavigate,Link} from 'react-router-dom';
import "./Login.css"
const accounts = [
  {email:'systemadmin@gmail.com', password:'sys', role:'system_admin', name:'System Admin User'},
  {email:'labadmin@gmail.com', password:'lab', role:'lab_admin', name:'Lab Admin User'},
  {email:'mentor@gmail.com', password:'men', role:'mentor', name:'Mentor User'},
  {email:'candidate@gmail.com', password:'can', role:'candidate', name:'Student User'},
  {email:'enterprise@gmail.com', password:'ent', role:'enterprise', name:'Enterprise User'},
];
export default function Login(){
    const [email, setEmail] =useState('');
    const [password, setPassword] =useState('');
    const [showPassword, setShowPassword] =useState(false);
    const [error,setError]=useState('');
    const navigate = useNavigate();
    const passwordRef=useRef();
    useEffect(() => {
    const userData = localStorage.getItem('user');
    if (userData) {
        const user = JSON.parse(userData);
        if (user.role === 'system_admin') {
            navigate('/system_admin', { replace: true });
        } else if (user.role === 'lab_admin') {
            navigate('/lab_admin', { replace: true });
        } else if (user.role === 'mentor') {
            navigate('/mentor', { replace: true });
        } else if (user.role === 'candidate') {
            navigate('/candidate', { replace: true });
        } else {
            navigate('/dashboard', { replace: true });
        } 
    }
    }, [navigate]);
    const handleSubmit =(e) =>{
        e.preventDefault();
        setError('');
        const account=accounts.find(
            acc=>acc.email===email && acc.password === password
        )
        if (!account) {
            setError('Invalid email or password!');
            return;
        }
        localStorage.setItem('user', JSON.stringify(account));
        if (account.role === 'system_admin') {
            navigate('/system_admin', { replace: true });
        } else if (account.role === 'lab_admin') {
            navigate('/lab_admin', { replace: true });
        } else if (account.role === 'mentor') {
            navigate('/mentor', { replace: true });
        } else if(account.role === 'candidate'){
            navigate('/candidate', { replace: true });
        } else if (account.role === 'enterprise') {
            navigate('/enterprise', { replace: true });
        }
    };

    return(     
        <div className="login-container">
            <div className="login-card">
                <div className="login-header">
                    <h1 className="title">
                        LabOdc
                    </h1>
                </div>
                {error && <div className="error-message">{error}</div>}
                <form onSubmit={handleSubmit} className="login-form">
                    <div className="form">
                        <label htmlfor="email" className="label-form">
                            Your email address
                        </label>
                        <div className="input-wrapper">
                            <input
                            type ="text"
                            id="email"
                            placeholder="email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            onKeyDown={(e)=>{
                                if(e.key==='Enter'){
                                    e.preventDefault();
                                    passwordRef.current.focus();
                                }
                            }
                            }
                            className="form-input"
                            />
                        </div>
                    </div>
                    <div className="form">
                        <label htmlfor="password" className="label-form">
                            Your password
                        </label>
                        <div className="input-wrapper">
                            <input
                            ref={passwordRef}
                            type={showPassword ? 'text' : 'password'}
                            id="password"
                            placeholder="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            className="form-input password-input"
                            />
                            <button
                            type="button"
                            onClick={() => setShowPassword(!showPassword)}
                            className="show"
                            >
                                {showPassword ? <EyeOff className="icon" /> : <Eye className="icon" />}
                            </button>
                        </div>
                    </div>
                    <div className="options">
                        <Link to="/forgot-password" className="forgot-link">
                            Forgot password?
                        </Link>
                    </div>
                    <button className="submit">
                        Login
                    </button>
                </form>
            </div>
        </div>
    );
}

