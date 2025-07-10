import axios from "axios";
var local = "http://localhost:5000/api";
var remote = "https://backend-dec-56b1.onrender.com/api";
const api = axios.create({
  baseURL: local,
  withCredentials: true,
});

export default api;
