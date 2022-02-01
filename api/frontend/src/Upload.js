import axios from 'axios';
import { BASE_URL } from './Dropdown'
import Button from 'react-bootstrap/Button';
import Container from 'react-bootstrap/Container';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Table from 'react-bootstrap/Table';
import modelo from './modelo.csv';
import Spinner from 'react-bootstrap/Spinner'
import React, { Component } from 'react';
import { darkGeneric, lightGeneric } from './themes';
import { Navigate } from "react-router-dom";
import styled from "styled-components";
import { analytics } from '.';
import { logEvent } from 'firebase/analytics';

const TooltipButton = styled(Button)`
  text-align: center;
`;
const TooltipBox = styled.div`
  position: absolute;
  top: calc(100% + 10px);
  // left: 30px;
  visibility: hidden;
  color: transparent;
  background-color: transparent;
  // width: 150px;
  padding: 5px 5px;
  border-radius: 4px;
  transition: visibility 0.5s, color 0.5s, background-color 0.5s, width 0.5s,
    padding 0.5s ease-in-out;
  &:before {
    content: "";
    width: 0;
    height: 0;
    // left: 40px;
    top: -10px;
    position: absolute;
    border: 10px solid transparent;
    transform: rotate(135deg);
    transition: border 0.3s ease-in-out;
  }
`;
const TooltipCard = styled.div`
  position: relative;
  & ${TooltipButton}:hover + ${TooltipBox} {
    visibility: visible;
    color: ${props => props.theme.color};
    background-color: ${props => props.theme.background};
    &:before {
      border-color: transparent transparent ${props => props.theme.background}
        ${props => props.theme.background};
    }
  }
`;


class Upload extends Component {
	constructor() {
		super();
		this.state = {
			redirect: '',
			isLoading: false,
			isDownloading: false,
			val:0,
			progress: 0,
			message: "",
			selectedFile: null
		};
	}
    
    // On file select (from the pop up)
  onFileChange = event => {
  
    // Update the state
    this.setState({ selectedFile: event.target.files[0] });
  
  };

	onFileUpload = async () => {
    if (this.state.selectedFile === null) {
      alert("Por favor, selecione algum arquivo");
      logEvent(analytics, 'upload', {
        error: true,
        message: 'sem_arquivo',
      });
      return;
    }
    const extension = this.state.selectedFile.name.slice(-4);
    console.log(extension);
    console.log(this.state.selectedFile.name);
    if (extension !== ".csv") {
      alert("Por favor, selecione um arquivo CSV");
      logEvent(analytics, 'upload', {
        error: true,
        message: 'non_csv',
      });
      return;
    }

		this.setState({ isLoading: true , val : 0});
		let currentFile = this.state.selectedFile;
	
		let formData = new FormData();

    formData.append("file", currentFile);
		
		const response = await axios.post(BASE_URL + "/api/uploadfile", formData)
    let error = false;
    let message;
    try {
      if (response.data.message.includes('faltando')) {
        error = true;
        message = 'sem_nome';
      }
      else
        message = 'sucesso';
			this.setState({ isLoading: false , val : 100 })
    }
    catch(e) {
      this.setState({ isLoading: false , val : 100 })
      alert("Erro ao fazer upload");
      error = true;
      message = 'problema_interno';
    }
    logEvent(analytics, 'upload', {
      error: error,
      message: message,
    });
	}

	downloadModelo = async () => {
    logEvent(analytics, 'download_modelo', {});
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

  downloadTabelaUsuario = async () => {
    this.setState({ isDownloading: true , val : 0});
    const req_options = {
      method: "GET",
    }

    fetch(BASE_URL + "/api/download-user-table", req_options)
    .then((response) => response.blob())
    .then((blob) => {
      // Create blob link to download
      const url = window.URL.createObjectURL(
        new Blob([blob]),
      );
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute(
        'download',
        'tabela_usuario.csv',
      );

      // Append to html link element page
      document.body.appendChild(link);

      // Start download
      link.click();

      // Clean up and remove the link
      link.parentNode.removeChild(link);
      this.setState({ isDownloading: false , val : 100});
      logEvent(analytics, 'download_usuario', {
        error: false,
      });
    })
    .catch(error => {
      alert("Ocorreu um problema com o Download");
      logEvent(analytics, 'download_usuario', {
        error: true,
      });
    });
  }

  voltar = () => {
    this.setState({redirect: '/'})
  }
    
  render() {
    if (this.state.redirect) {
      return <Navigate to={this.state.redirect} />
		}
    return (
		<Container fluid style={{height: "inherit"}}>
			<Table striped bordered hover>
			<thead>
				<tr>
          <td align='center' colSpan = "5">
            <h3>Formato de csv aceito</h3>
            {/* <br></br> */}
            <h3>(separado por ",")</h3>
            </td>
          </tr>
				<tr>
				<th>nome</th>
				<th>estado</th>
				<th>cidade</th>
				<th>mercado</th>
				<th>stacks</th>
				</tr>
				<tr>
				<td align='left' colSpan = "5">
        <div style={{ display: 'flex', gap: '10px', justifyContent: 'center' }}>
          <TooltipCard style={{ flex: '1 1 50%' }}
          theme={ this.props.theme === 'light' ? darkGeneric : lightGeneric }>
            <TooltipButton
            className={this.props.theme === 'light' ? 'btn-primary' : 'btn-info'}
            style={{ width: '100%'}}
            data-testid="downloadModelo"
            variant="primary"
            onClick={ this.downloadModelo }>
              Modelo CSV
            </TooltipButton>
            <TooltipBox data-testid="modelo-descricao">
              Clique aqui para baixar o modelo
              de CSV vazio aceito pelo programa
            </TooltipBox>
          </TooltipCard>
          <TooltipCard style={{ flex: '1 1 50%' }}
          theme={ this.props.theme === 'light' ? darkGeneric : lightGeneric }>
            <TooltipButton
            className={this.props.theme === 'light' ? 'btn-primary' : 'btn-info'}
            style={{ width: '100%'}}
            data-tip='React-tootltip'
            data-testid="downloadUsuario"
            variant="primary"
            onClick={ this.downloadTabelaUsuario }>
            {this.state.isDownloading && <Spinner
            as="span"
            animation="grow"
            size="sm"
            role="status"
            aria-hidden="true"
            />}
            Tabela do Usuário
          </TooltipButton>
            <TooltipBox data-testid="usuario-descricao">
              Clique aqui para baixar uma tabela
              com todos os dados adicionados pelos
              usuários
            </TooltipBox>
          </TooltipCard>
        </div>
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
          className={this.props.theme === 'light' ? 'btn-primary' : 'btn-info'}
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
        className={this.props.theme === 'light' ? 'btn-primary' : 'btn-info'}
				data-testid="download"
				variant="primary"
				onClick={this.voltar}>
					Voltar...
				</Button>
				</Col>
			</Row>
		</Container>
    );
    }
  }
 
  export default Upload;