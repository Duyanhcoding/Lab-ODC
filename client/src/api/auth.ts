import api from './axios';

export const authAPI = {
  register: async (data: {
    email: string;
    password: string;
    full_name: string;
    role: string;
  }) => { console.log('Sending register request with data:', data);
    
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
  console.log('send Login Request');
  try{
    const response =await api.post('/auth/Login', form,{
      headers:{
        'Content-Type':'application/x-www-form-urlencoded',
      },
    });
    console.log('Login response:',response.data);
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
  forgotPassword: async (email: string) => {
    return await api.post('/auth/forgot-password', { email });
  },

  resetPassword: async (data: { token: string; password: any }) => {
    return await api.post('/auth/reset-password', data);
  }
};