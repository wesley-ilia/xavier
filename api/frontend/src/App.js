import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Consulta from './Consulta';
import Upload from './Upload';
import Home from './Home';
import Button from 'react-bootstrap/Button';
// import { lightTheme, darkTheme } from "./themes";
import './App.css'
import { ThemeProvider } from "styled-components";
// import useLocalStorage from 'use-local-storage'
const darkTheme = {
	pageBackground: "#111",  
	titleColor: "#fafafa",  
	tagLineColor: "#6B8096"
}; 

class App extends Component {
  
  constructor() {
    // this.defaultDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    super();
    this.state = {
      theme: 'dark',
      name: 'React'
    };
  }
  /* [this.theme, this.setTheme] = useLocalStorage('theme', this.defaultDark ? 'dark' : 'light'); */
  switchTheme = () => {
    const newTheme = this.state.theme === 'light' ? 'dark' : 'light';
    this.setState({ theme: newTheme });
    console.log(this.state.theme);
  }

  toggleTheme = () => {
    console.log(this.state.theme)
    if (this.state.theme === "light") {
      window.localStorage.setItem("theme", "dark");
      this.setState({theme: "dark"});
    } else {
      window.localStorage.setItem("theme", "light");
      this.setState({theme: "light"});
    }
  };
  
  render() {
    return (
      <ThemeProvider theme={darkTheme}>
      <Button
      data-testid="download"
      variant="primary"
      onClick={ this.toggleTheme }>
        Theme
      </Button>
      <Router>
			<div className='app'>
			<Routes>
				<Route exact path="/" element={<Consulta/>}/>
				<Route exact path="/consulta" element={<Consulta/>}/>
				<Route exact path="/upload" element={<Upload/>}/>
			</Routes>
			</div>
		</Router>
    </ThemeProvider>
    );
  }
}

export default App;
  