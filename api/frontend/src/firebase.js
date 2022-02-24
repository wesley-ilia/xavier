import axios from "axios";
import { BASE_URL } from "./Dropdown";
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";

export const getFirebaseCredentials = async () => {
  let response = await axios.get(BASE_URL + "/api/get_env");
  const data = await response.data;

  try {
    const firebaseConfig = {
      apiKey: data.apiKey,
      authDomain: data.authDomain,
      projectId: data.projectId,
      storageBucket: data.storageBucket,
      messagingSenderId: data.messagingSenderId,
      appId: data.appId,
      measurementId: data.measurementId,
    };
    const app = initializeApp(firebaseConfig);
    return getAnalytics(app);
  } catch {
    return "Error";
  }
};
