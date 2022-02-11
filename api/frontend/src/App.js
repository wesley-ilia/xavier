import React, { Component } from "react";
import Figure from "react-bootstrap/Figure";
import Consulta from "./Consulta";
import { Appearance } from 'react-native';
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional

const firebaseConfig = {
  apiKey: process.env.REACT_APP_APIKEY,
  authDomain: process.env.REACT_APP_AUTHDOMAIN,
  projectId: process.env.REACT_APP_PROJECTID,
  storageBucket: process.env.REACT_APP_STORAGEBUCKET,
  messagingSenderId: process.env.REACT_APP_MESSAGINGSENDERID,
  appId: process.env.REACT_APP_APPID,
  measurementId: process.env.REACT_APP_MEASUREMENTID,
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export var analytics = getAnalytics(app);

const flexBox = {
  display: "flex",
  justifyContent: "flex-start" /* adjustment */,
  position: "relative" /* new */,
  marginBottom: "20px",
};

const alignRight = {
  flex: "0 1 auto",
  width: "100px",
  height: "100px",
  marginLeft: "auto" /* new */,
  marginTop: "10px",
};

const alignCenter = {
  flex: "0 1 auto",
  position: "absolute" /* new */,
  left: "50%",
  transform: "translateX(-50%)",
};

class App extends Component {
  constructor() {
    super();

    this.state = {
      theme: Appearance.getColorScheme(),
    };
  }

  Sol = () => {
    return (
      <Figure style={alignRight}>
        <Figure.Image
          onClick={this.toggleTheme}
          width={30}
          height={30}
          src="./sol.png"
        />
      </Figure>
    );
  };

  Lua = () => {
    return (
      <Figure style={alignRight}>
        <Figure.Image
          onClick={this.toggleTheme}
          width={30}
          height={30}
          src="./lua.png"
        />
      </Figure>
    );
  };

  switchTheme = () => {
    const newTheme = this.state.theme === "light" ? "dark" : "light";
    this.setState({ theme: newTheme });
  };

  toggleTheme = () => {
    if (this.state.theme === "light") {
      window.localStorage.setItem("theme", "dark");
      this.setState({ theme: "dark" });
    } else {
      window.localStorage.setItem("theme", "light");
      this.setState({ theme: "light" });
    }
    localStorage.setItem("theme", this.state.theme);
  };

  render() {
    return (
      <div>
        <div style={flexBox}>
          {this.state.theme === "light" ? <this.Lua /> : <this.Sol />}
          <Figure style={alignCenter}>
            <Figure.Image width={150} height={150} src="./logo.png" />
          </Figure>
        </div>
        <Consulta theme={this.state.theme} />
      </div>
    );
  }
}

export default App;
