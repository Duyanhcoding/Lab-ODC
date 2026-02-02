import api from './axios';

export const authAPI = {
  register: async (data: {
    email: string;
    password: string;
    full_name: string;
    role: string;
  }) => {
    console.log('Sending register request with data:', data);
    
    try {
      const response = await api.post('/auth/register', data);
      console.log('Register response:', response.data);
      return response;
    } catch (error: any) {
      console.error('Register error details:', {
        message: error.message,
        response: error.response?.data,
        status: error.response?.status
      });
      throw error;
    }
  },

  login: async (data: { email: string; password: string }) => {
    const form = new URLSearchParams();
    form.append('username', data.email);
    form.append('password', data.password);

    console.log('Sending login request');
    
    try {
      const response = await api.post('/auth/login', form, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      });
      console.log('Login response:', response.data);
      return response;
    } catch (error: any) {
      console.error('Login error details:', {
        message: error.message,
        response: error.response?.data,
        status: error.response?.status
      });
      throw error;
    }
  },

  forgotPassword: async (data: { email: string }) => {
    console.log('Sending forgot password request for:', data.email);
    
    try {
      const response = await api.post('/auth/forgot-password', data);
      console.log('Forgot password response:', response.data);
      return response;
    } catch (error: any) {
      console.error('Forgot password error details:', {
        message: error.message,
        response: error.response?.data,
        status: error.response?.status
      });
      throw error;
    }
  },

  // Reset Password - đặt lại mật khẩu với token
  resetPassword: async (data: { token: string; new_password: string }) => {
    console.log('Sending reset password request');
    
    try {
      const response = await api.post('/auth/reset-password', data);
      console.log('Reset password response:', response.data);
      return response;
    } catch (error: any) {
      console.error('Reset password error details:', {
        message: error.message,
        response: error.response?.data,
        status: error.response?.status
      });
      throw error;
    }
  }
};
