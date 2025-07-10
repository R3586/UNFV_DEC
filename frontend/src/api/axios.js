import axios from "axios";
var local = "http://localhost:5000/api";
var remote = "https://unfv-dec-7xrz.onrender.com/api";
const api = axios.create({
  baseURL: remote,
  withCredentials: true, // Envía cookies y headers de autenticación
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  }
});

// Interceptor para manejar errores de CORS
api.interceptors.request.use(
  config => {
    // Agrega headers adicionales si es necesario
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

// Interceptor para respuestas
api.interceptors.response.use(
  response => response,
  error => {
    if (error.response && error.response.status === 401) {
      // Manejar errores de autenticación
      console.error('No autorizado - redirigir a login');
    }
    return Promise.reject(error);
  }
);

export default api;
