import axios from 'axios';

const baseDomain = "http://127.0.0.1:8000"
const baseURL = `${baseDomain}/api/v1`;

export default axios.create({
    baseURL
})