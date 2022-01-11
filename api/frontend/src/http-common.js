import { BASE_URL } from "./Dropdown";
import axios from "axios";

export default axios.create({
  baseURL: BASE_URL,
  headers: {
    "Content-type": "application/json"
  }
});
