import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Consulta from './Consulta';
import Upload from './Upload';
import Home from './Home';

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
			<div>
			<Routes>
				<Route exact path="/" element={<Consulta/>}/>
				<Route exact path="/consulta" element={<Consulta/>}/>
				<Route exact path="/upload" element={<Upload/>}/>
			</Routes>
			</div>
		</Router>
    );
  }
}

export default App;
  