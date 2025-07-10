import axios from "axios";
var local = "http://localhost:5000/api";
var remote = "https://unfv-dec.onrender.com";
const api = axios.create({
  baseURL: remote,
  withCredentials: true,
});

export default api;
