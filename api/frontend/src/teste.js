import React, { Component } from 'react';
import { render } from 'react-dom';
import { BrowserRouter as Router, Route, Link, Routes } from 'react-router-dom';
import Consulta from './App';
import Upload from './Upload';

const Nav = () => (
  <div>
    <ul>
      <li><Link to="/consulta">Consulta</Link></li>
      <li><Link to="/upload">Upload</Link></li>
    </ul>
  </div>
);

class App extends Component {
  constructor() {
    super();
    this.state = {
      name: 'React'
    };
  }

  render() {
    return (
      <Router>

        {/* Router component can have only 1 child. We'll use a simple
          div element for this example. */}
        <div>
          <Nav />
        <Routes>
            <Route exact path="/consulta" element={<Consulta/>}/>
            <Route path="/upload" element={<Upload/>}/>
            <Route path="/" element={<Home/>}/>		 
        </Routes>
        </div>
      </Router>
    );
  }
}

export default App;