import React, { Component } from 'react';
import Card from 'react-bootstrap/Card';
import Figure from 'react-bootstrap/Figure'
import { ThemeProvider } from 'styled-components';
import Consulta from './Consulta';
import { GlobalStyle } from './themes'

class App extends Component {
  constructor () {
    super();

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
    return (
      <div style={{ display: 'flex', gap: '10px', justifyContent: 'center' }}>
      <ThemeProvider theme={{ mode: this.state.theme }}>
      <>
        <GlobalStyle />
        <Consulta style={{ flex: '1 1 1' }} />
    </>
    </ThemeProvider>
    </div>
    );
  }
}

export default App;