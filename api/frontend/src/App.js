import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Consulta from './Consulta';
import Upload from './Upload';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import Figure from 'react-bootstrap/Figure'
import './App.css'
import { ThemeProvider } from 'styled-components';
import { GlobalStyle } from './themes'

class App extends Component {
  
  constructor() {
    // this.defaultDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    super();
    this.state = {
      theme: 'light',
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
      <ThemeProvider theme={{ mode: this.state.theme }}>
      <>
        <GlobalStyle />
      <Button
      data-testid="download"
      variant="primary"
      onClick={ this.toggleTheme }>
        Theme
      </Button>
      <Card data-testid="card"  style={{ width: '35%', height: "100%", marginLeft: "auto", marginRight: "auto" }}>
          <Card.Body style={{height: "100%"}}>
              <center>
                  <Figure>
                  <Figure.Image
                    width={200}
                    height={200}
                    src="./Xavier_1_1.png"
                  />
                  </Figure>
              </center>
      <Router>
			<div className='app'>
			<Routes>
				<Route exact path="/" element={<Consulta theme={this.state.theme}/>}/>
				<Route exact path="/consulta" element={<Consulta theme={this.state.theme}/>}/>
				<Route exact path="/upload" element={<Upload theme={this.state.theme}/>}/>
			</Routes>
			</div>
		</Router>
    </Card.Body>
    </Card>
    </>
    </ThemeProvider>
    );
  }
}

export default App;