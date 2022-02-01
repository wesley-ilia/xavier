import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Consulta from './Consulta';
import Upload from './Upload';
import Card from 'react-bootstrap/Card';
import Figure from 'react-bootstrap/Figure'
import { ThemeProvider } from 'styled-components';
import { GlobalStyle } from './themes'
import { Appearance } from 'react-native';

class App extends Component {
  constructor () {
    super();
    
    this.state = {
      theme: Appearance.getColorScheme(),
      name: 'React',
      width: window.innerWidth,
    };
  }

  handleResize = () => {
    this.setState({ width: window.innerWidth });
  }

  Sol = () => {
    return (
      <Figure>
        <Figure.Image onClick={ this.toggleTheme }
          width={30}
          height={30}
          src="./sol.png"
        />
      </Figure>
    );
  }
  
  Lua = () => {
    return (
      <Figure>
        <Figure.Image onClick={ this.toggleTheme }
          width={30}
          height={30}
          src="./lua.png"
        />
      </Figure>
    );
  }
  
  switchTheme = () => {
    const newTheme = this.state.theme === 'light' ? 'dark' : 'light';
    this.setState({ theme: newTheme });
  }

  toggleTheme = () => {
    if (this.state.theme === "light") {
      window.localStorage.setItem("theme", "dark");
      this.setState({theme: "dark"});
    } else {
      window.localStorage.setItem("theme", "light");
      this.setState({theme: "light"});
    }
    localStorage.setItem('theme', this.state.theme);
  };
  
  render() {
    window.addEventListener('resize', this.handleResize);
    return (
      <div>
      <ThemeProvider theme={{ mode: this.state.theme }}>
      <>
        <GlobalStyle />
      
      <Card data-testid="card"  style={{ width: '35%', height: "100%", marginLeft: "auto", marginRight: "auto" }}>
          <Card.Body style={{height: "100%"}}>
          {this.state.theme === 'light' ? <this.Lua/> : <this.Sol/>}
          
          </Card.Body>
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
    </div>
    );
  }
}

export default App;