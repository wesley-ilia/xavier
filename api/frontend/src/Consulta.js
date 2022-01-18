import React from 'react';
import Select from 'react-select';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Dropdown, { BASE_URL } from './Dropdown'
import 'bootstrap/dist/css/bootstrap.min.css';
import { getCidades } from './Utils';
import { darkSelect, lightSelect, darkGeneric, lightGeneric } from './themes';
import { Navigate } from "react-router-dom";


var i;

class Consulta extends React.Component {
  constructor() {
    console.log(localStorage.getItem('theme'));
    super();
    this.estadosExecute = [];
    this.mercadosExecute = [];
    this.stacksExecute = [];
    this.cidadesExecute = [];
    this.colunasExecute = ['nome', 'estado', 'cidade', 'mercado', 'stacks'];
    this.capitais = 'sim';
    this.state = {
      redirect: '',
      cardTheme: "card bg-light mb-3",
      preview: "0",
      cidades: [],
      showCidades: false,
    }
    this.fileName = "Untitled";
    this.extension = "csv";
    this.dropdown = new Dropdown();
  }

  download = async () => {
    const req_options = {
      method: "GET",
    }
    if (this.mercadosExecute.length === 0 && this.estadosExecute.length === 0
      && this.stacksExecute.length === 0) {
      alert("Preencha algum campo");
      return;
    }
    await fetch(BASE_URL + "/search?market="+this.mercadosExecute
    +"&stack="+this.stacksExecute+"&state="+this.estadosExecute+"&extension="+this.extension
    +"&cidade="+this.cidadesExecute+"&capitais="+this.capitais+"&colunas="+this.colunasExecute,
    req_options)
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
        this.fileName + '.' + this.extension,
      );

      // Append to html link element page
      document.body.appendChild(link);

      // Start download
      link.click();

      // Clean up and remove the link
      link.parentNode.removeChild(link);
    });

  }

  getPreview = async () => {
    const req_options = {
      method: "GET",
    }
    const response = await fetch(BASE_URL + "/preview?market="+this.mercadosExecute
    +"&stack="+this.stacksExecute+"&state="+this.estadosExecute+"&cidade="+this.cidadesExecute
    +"&capitais="+this.capitais,
    req_options);
    
    const data = await response.json();
    this.setState({preview: data})
  };

  handleChangeEstados = e => {
    var values = [];
    for (i = 0; i < e.length; i++)
      values.push(e[i].value);
    this.estadosExecute = [...values];
    this.getPreview();
    if (this.state.showCidades)
      getCidades(this);
  }

  handleChangeCidades = e => {
    var values = [];
    for (i = 0; i < e.length; i++)
      values.push(e[i].value);
    this.cidadesExecute = [...values];
    this.getPreview();
  }

  handleChangeMercados = e => {
    var values = [];
    for (i = 0; i < e.length; i++)
      values.push(e[i].value);
    this.mercadosExecute = [...values];
    this.getPreview();
  }
  

  handleChangeColunas = e => {
    var values = [];
    for (i = 0; i < e.length; i++)
      values.push(e[i].value);
    this.colunasExecute = [...values];
  }

  handleChangeStacks = e => {
    var values = [];
    for (i = 0; i < e.length; i++)
      values.push(e[i].value.replace("C++", "Cpp").replace("C#", "Csharp"));
    this.stacksExecute = [...values];
    this.getPreview();
  }

  handleChangeFile = e => {
    if (e.target.value === "")
      this.fileName = "Untitled";
    else
      this.fileName = e.target.value;
  }

  handleChangeExtension = e => {
    this.extension = e.value;
  }

  handleCidadesRadio = e => {
    this.capitais = e.target.value;
    if (e.target.value === "esp") {
      this.setState({showCidades: true});
      getCidades(this);
    }
    else {
      for (i = 0; this.cidadesExecute.length > 0; i++)
        this.cidadesExecute.splice(0, 1);
      this.setState({showCidades: false});
    }
    this.getPreview();
  }

  upload = () => {
    this.setState({redirect: '/upload'})
  }

  render () {
    if (this.state.redirect) {
      return <Navigate to={this.state.redirect} />
    }
    return (
      <div className="Consulta">
        <Container fluid style={{height: "inherit"}}>
          <Row>
            <Col>
            <form data-testid="form-estados">
              <label htmlFor="estados"><h2>Estados</h2></label>
              <Select
              styles={ this.props.theme === 'light' ? lightSelect: darkSelect }
              classNamePrefix='estados'
              name="estados"
              inputId="estados"
              options={this.dropdown.estados}
              isMulti
              onChange={ this.handleChangeEstados }
              />
            </form>
            </Col>
          </Row>
          <form data-testid="form-cidades">
          <label htmlFor="cidades"><h2>Cidades</h2></label>
          <Row>
            <Col>
              <input type="radio" className="btn-check" id="btnradio1" value="sim" name="capitais" defaultChecked
              onChange={ this.handleCidadesRadio }></input>
              <label className="btn btn-outline-primary" htmlFor="btnradio1"><h7>Com Capitais</h7></label>
            </Col>
            <Col>
              <input type="radio" className="btn-check" id="btnradio2" value="nao" name="capitais"
              onChange={ this.handleCidadesRadio }></input>
              <label className="btn btn-outline-primary" htmlFor="btnradio2"><h7>Sem Capitais</h7></label>
            </Col>
            <Col>
              <input type="radio" className="btn-check" id="btnradio3" value="esp" name="capitais"
              onChange={ this.handleCidadesRadio }></input>
              <label className="btn btn-outline-primary" htmlFor="btnradio3"><h7>Específicas</h7></label>
            </Col>
          </Row>
          { this.state.showCidades && <Row style={{paddingTop: '10px'}}>
            <Col data-testid="cidades-drop">
              <Select
              styles={ this.props.theme === 'light' ? lightSelect: darkSelect }
              classNamePrefix='cidades'
              name="cidades"
              inputId="cidades"
              options={ this.state.cidades }
              isMulti
              onChange={ this.handleChangeCidades }
              />
            </Col>
          </Row>}
          </form>
          <Row>
            <Col>
            <form data-testid="form-mercados">
              <label htmlFor="mercados"><h2>Mercados</h2></label>
              <Select
              styles={ this.props.theme === 'light' ? lightSelect: darkSelect }
              classNamePrefix='mercados'
              name="mercados"
              inputId="mercados"
              options={ this.dropdown.mercados }
              isMulti
              onChange={ this.handleChangeMercados }
              />
            </form>
            </Col>
          </Row>
          <Row>
            <Col>
            <form data-testid="form-stacks">
              <label htmlFor="stacks"><h2>Stacks</h2></label>
              <Select
              styles={ this.props.theme === 'light' ? lightSelect: darkSelect }
              classNamePrefix='stacks'
              name="stacks"
              inputId="stacks"
              options={ this.dropdown.stacks }
              isMulti
              onChange={ this.handleChangeStacks }
              />
            </form>
            </Col>
          </Row>
          <Row>
            <Col>
            <form data-testid="form-colunas">
              <label htmlFor="colunas"><h2>Colunas</h2></label>
              <Select
              styles={ this.props.theme === 'light' ? lightSelect: darkSelect }
              defaultValue={[
                { label: "nome" , value: "nome" },
                { label: "estado", value: "estado" },
                { label: "cidade", value: "cidade" },
                { label: "mercado", value: "mercado" },
                { label: "stacks", value: "stacks" }
              ]}
              classNamePrefix='colunas'
              name="colunas"
              inputId="colunas"
              options={ this.dropdown.colunas }
              isMulti
              onChange={ this.handleChangeColunas }
              />
            </form>
            </Col>
          </Row>
          <Row>
            <Col>
              <div id="preview" style={{marginTop: "10px", marginBottom: "10px"}}>
                <label htmlFor="previer"><h5>Preview: { this.state.preview } </h5></label>
              </div>
            </Col>
          </Row>
          <Row>
            <Col>Nome do arquivo</Col>
          </Row>
          <Row>
            <Col xs lg="7" >
              <Form.Control name="teste" placeholder="Nome do arquivo"
              onChange={ this.handleChangeFile } style={ this.props.theme === 'light' ? lightGeneric : darkGeneric }/>
            </Col>
            <Col xs lg="4">
            <form data-testid='file-Type'>
              <label hidden data-testid='label-type' htmlFor='fileType'>type</label>
                <Select
                styles={ this.props.theme === 'light' ? lightSelect: darkSelect }
                classNamePrefix='fileType'
                name='fileType'
                inputId='fileType'
                options={[
                  {label: ".csv", value: "csv"},
                  {label: ".xlsx", value: "xlsx"},
                  {label: ".pdf", value: "pdf"},
                ]}
                defaultValue={{ label: ".csv", value: "csv" }}
                onChange={ this.handleChangeExtension }
                style={{width: "50%"}}
                />
              </form>
            </Col>
          </Row>
          <Row>
            <Col style={{marginTop:"10px"}}>
              <Button
              data-testid="download"
              variant="primary"
              style={{marginLeft: "0px"}}
              onClick={ this.download }>
                Download
              </Button>
            </Col>
          </Row>
          <Row>
            <Col style ={{ paddingTop: "10px" }}>
              <Button
              data-testid="upload"
              variant="primary"
              onClick={ this.upload }>
                Upload...
              </Button>
            </Col>
          </Row>
        </Container>
      </div>
    );
  }
}

export default Consulta;
