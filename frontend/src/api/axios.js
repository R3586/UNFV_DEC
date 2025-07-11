import axios from "axios";
var local = "http://localhost:5000/api";
var remote = "https://unfv-dec.onrender.com/api";
const api = axios.create({
  baseURL: remote,
  withCredentials: true,
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  }
});
export default api;
