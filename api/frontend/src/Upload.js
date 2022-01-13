import axios from 'axios';
import { BASE_URL } from './Dropdown'
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import Container from 'react-bootstrap/Container';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Table from 'react-bootstrap/Table';
import modelo from './modelo.csv';
import Spinner from 'react-bootstrap/Spinner'
import ProgressBar from 'react-bootstrap/ProgressBar'
import React, { Component } from 'react';
import { darkSelect, lightSelect, darkGeneric, lightGeneric } from './themes';
 
class Upload extends Component {
	
	
    state = {
		isLoading: false,
		val:0,
		progress: 0,
		message: "",
    	selectedFile: null
    };
    
    // On file select (from the pop up)
    onFileChange = event => {
    
      // Update the state
      this.setState({ selectedFile: event.target.files[0] });
    
    };

	onFileUpload = async () => {
		this.setState({ isLoading: true , val : 0});
		let currentFile = this.state.selectedFile;
	
		let formData = new FormData();

    	formData.append("file", currentFile);
		
		axios.post(BASE_URL + "/api/uploadfile", formData)
		.then(response => {
			this.setState({ isLoading: false , val : 100})

		});
	}

	download = async () => {
		const link = document.createElement('a');
		link.href = modelo;
		link.setAttribute(
		'download',
		'modelo.csv',
		);

		// Append to html link element page
		document.body.appendChild(link);

		// Start download
		link.click();

		// Clean up and remove the link
		link.parentNode.removeChild(link);
	};

	voltar = () => {
		const link = document.createElement('a');
		link.href = '/';

		// Append to html link element page
		document.body.appendChild(link);

		// Start download
		link.click();

		// Clean up and remove the link
		link.parentNode.removeChild(link);
	};
    
    // File content to be displayed after
    // file upload is complete
    
    render() {
    
      return (
                <Container fluid style={{height: "inherit"}}>
					<Table striped bordered hover style={ this.props.theme === 'light' ? lightGeneric: darkGeneric }>
					<thead>
                        <tr><td align='center' colSpan = "5"><h3>Formato de csv aceito</h3><br></br><h10>separado por ','</h10></td></tr>
						<tr>
						<th>nome</th>
						<th>estado</th>
						<th>cidade</th>
						<th>mercado</th>
						<th>stacks</th>
						</tr>
                        <tr>
						<td align='left' colSpan = "5">
							<Button
							data-testid="download"
							variant="primary"
							onClick={ this.download }>
								Download Modelo csv
							</Button>
						</td>
                        </tr>
					</thead>
					</Table>
                    <Row style={{ paddingTop: "10px"}}>
                        <Col xs lg="9">
                            <Form.Control type="file" style={ this.props.theme === 'light' ? lightGeneric: darkGeneric } onChange={this.onFileChange} />
                        </Col>
						<Col xs lg="2">
                            <Button
                            data-testid="download"
                            variant="primary"
                            onClick={ this.onFileUpload }>
                                {this.state.isLoading && <Spinner
									as="span"
									animation="grow"
									size="sm"
									role="status"
									aria-hidden="true"
									/>}
							Upload!
                            </Button>
						</Col>
						<Spinner type="Circles" color="#00BFFF" height={80} width={80}/>
					</Row>
					<Row style={{paddingTop: '10px'}}>
						<Col>
						<Button
						data-testid="download"
						variant="primary"
						onClick={this.voltar}>
							Voltar
						</Button>
						</Col>
					</Row>
                </Container>
      );
    }
  }
 
  export default Upload;