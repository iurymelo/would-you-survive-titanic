import axios from 'axios'

const api = axios.create({
  baseURL: '0.0.0.0:9000'
});

export default api;
