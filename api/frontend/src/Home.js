import React, { Component } from 'react';
import Button from 'react-bootstrap/Button';

class Home extends Component {
	consulta = () => {
		const link = document.createElement('a');
		link.href = '/consulta';

		// Append to html link element page
		document.body.appendChild(link);

		// Start download
		link.click();

		// Clean up and remove the link
		link.parentNode.removeChild(link);
	};

	upload = () => {
		const link = document.createElement('a');
		link.href = '/upload';

		// Append to html link element page
		document.body.appendChild(link);

		// Start download
		link.click();

		// Clean up and remove the link
		link.parentNode.removeChild(link);
	};

	render () {
		return (
			<div align='center'>
				<Button
				variant="primary"
				onClick={this.consulta}>
					Consulta
				</Button>
				<Button
				variant="primary"
				onClick={this.upload}>
					Upload
				</Button>
			</div>
		);
	}		
}

export default Home;