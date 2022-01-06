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
 
import React, { Component } from 'react';
 
class Upload extends Component {
  
    state = {
 
      // Initially, no file is selected
      selectedFile: null
    };
    
    // On file select (from the pop up)
    onFileChange = event => {
    
      // Update the state
      this.setState({ selectedFile: event.target.files[0] });
    
    };
    
    // On file upload (click the upload button)
    onFileUpload = () => {
    
      // Create an object of formData
      const formData = new FormData();
    
      // Update the formData object
      formData.append(
        "file",
        this.state.selectedFile,
        this.state.selectedFile.name
      );
    
      // Details of the uploaded file
      console.log(this.state.selectedFile);
    
      // Request made to the backend api
      // Send formData object
      axios.post(BASE_URL + "/api/uploadfile", formData);
    };

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
		<Card data-testid="card" style={{ width: '35%', height: "100%", marginLeft: "auto", marginRight: "auto" }}>
            <Card.Body style={{height: "100%"}}>
                <Container fluid style={{height: "inherit"}}>
					<Table striped bordered hover>
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
							onClick={this.download}>
								Download Modelo csv
							</Button>
						</td>
                        </tr>
					</thead>
					</Table>
                    <Row style={{ paddingTop: "10px"}}>
                        <Col xs lg="9">
                            <Form.Control type="file" onChange={this.onFileChange} />
                        {/*  <input type="file" onChange={this.onFileChange} /> */}
                        </Col>
						<Col xs lg="2">
                            <Button
                            data-testid="download"
                            variant="primary"
                            onClick={this.onFileUpload}>
                                Upload!
                            </Button>
						</Col>
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
            </Card.Body>
        </Card>
      );
    }
  }
 
  export default Upload;