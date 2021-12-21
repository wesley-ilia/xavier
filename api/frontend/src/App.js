import React from 'react';
import Select from 'react-select';
/* import { Button } from 'react-native'; */
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import Form from 'react-bootstrap/Form';
import Stack from 'react-bootstrap/Stack';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';

import 'bootstrap/dist/css/bootstrap.min.css';
import Col from 'react-bootstrap/esm/Col';

var estados_ori = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO', 'TODOS'];

/* var fileOptions = [
  {label: ".csv", value: ".csv"},
  {label: ".xml", value: ".xml"}
] */

var i;

class App extends React.Component {
  constructor() {
    super();
    this.estadosExecute = [];
    this.mercadosExecute = [];
    this.stacksExecute = [];
    this.cidadesExecute = [];
    this.preview = '0';
    this.estados = [];
    this.mercados = [];
    this.cidades = [];
    this.stacks = [];
    this.state = {
      preview: "0",
    }
    this.fileName = "Untitled";
    this.extension = "csv"
    this.getDropdown()
  }

  getDropdown = async () => {
    const req_options = {
      method: "GET",
    }
    const response = await fetch("http://localhost:8000/dropdown", req_options);
    const data = response.json();
    var that = this;
    data.then(function(resp) {
      for (i = 0; i < resp.mercados.length; i++) {
        that.mercados.push({
          label: resp.mercados[i],
          value: resp.mercados[i]
        });
      }

      for (i = 0; i < resp.stacks.length; i++) {
        that.stacks.push({
          label: resp.stacks[i],
          value: resp.stacks[i]
        });
      }
      for (i = 0; i < estados_ori.length; i++) {
        that.estados.push({
          label: estados_ori[i],
          value: estados_ori[i]
        });
      }
    })
  };

  download = async () => {
    const req_options = {
      method: "GET",
    }
    if (this.mercadosExecute.length === 0 && this.estadosExecute.length === 0
      && this.stacksExecute.length === 0) {
      alert("Preencha algum campo");
      return;
    }
    await fetch("http://localhost:8000/search?get_csv=true&market="+this.mercadosExecute
    +"&stack="+this.stacksExecute+"&state="+this.estadosExecute+"&extension="+this.extension,
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
    const response = await fetch("http://localhost:8000/search?get_csv=false&market="+this.mercadosExecute
    +"&stack="+this.stacksExecute+"&state="+this.estadosExecute, req_options);
    
    const data = response.json();
    var that = this;
    data.then(function(resp) {
      that.setState({preview: resp});
    })
  };

  /* getCidades = async () => {
    const req_options = {
      method: "GET",
    }
    const response = await fetch("http://localhost:8000/search?get_csv=false&market="+this.mercadosExecute
    +"&stack="+this.stacksExecute+"&state="+this.estadosExecute, req_options);
  } */

  handleChangeEstados = e => {
    var values = [];
    for (i = 0; i < e.length; i++)
      values.push(e[i].value);
    this.estadosExecute = [...values];
    this.getPreview();
    this.getCidades();
  }

  handleChangeMercados = e => {
    var values = [];
    for (i = 0; i < e.length; i++)
      values.push(e[i].value);
    console.log(values)
    this.mercadosExecute = [...values];
    this.getPreview();
  }

  handleChangeStacks = e => {
    var values = [];
    for (i = 0; i < e.length; i++)
      values.push(e[i].value.replace("C++", "Cpp").replace("C#", "Csharp"));
    console.log(values)
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

  /* useEffect(() => {
    getDropdown();
  }, []) */
  render () {
    return (
      <div className="App">
        <Card style={{ width: '35%', height: "100%", marginLeft: "auto", marginRight: "auto" }}>
          <Card.Body style={{height: "100%"}}>
            <Container fluid style={{height: "inherit"}}>
              <Row >
                <Col><h2>Estados</h2></Col>
              </Row>
              <Row>
                <Col>
                  <Select
                  options={this.estados}
                  isMulti
                  onChange={ this.handleChangeEstados }
                  />
                </Col>
              </Row>
              <Row >
                <Col><h2>Cidades</h2></Col>
              </Row>
              <Row>
                <Col>
                  <Select
                  options={this.cidades}
                  isMulti
                  onChange={ this.handleChangeCidades }
                  />
                </Col>
              </Row>
              <Row>
                <Col><h2>Mercados</h2></Col>
              </Row>
              <Row>
                <Col>
                  <Select
                    options={this.mercados}
                    isMulti
                    onChange={ this.handleChangeMercados }
                  />
                </Col>
              </Row>
              <Row>
                <Col><h2>Stacks</h2></Col>
              </Row>
              <Row>
                <Col>
                  <Select
                    options={this.stacks}
                    isMulti
                    onChange={ this.handleChangeStacks }
                  />
                </Col>
              </Row>
              <Row>
                <Col>
                  {this.preview && <div style={{marginTop: "10px", marginBottom: "10px"}}>
                    <div>Preview: { this.state.preview }</div>
                  </div>}
                </Col>
              </Row>
              <Row>
                <Col>Nome do arquivo</Col>
              </Row>
              <Row>
                <Col xs lg="7" >
                  <Form.Control placeholder="Nome do arquivo"
                  onChange={ this.handleChangeFile }/>
                </Col>
                <Col xs lg="4">
                  <Select
                  options={[{label: ".csv", value: "csv"}, {label: ".xlsx", value: "xlsx"}]}
                  defaultValue={{ label: ".csv", value: "csv" }}
                  onChange={ this.handleChangeExtension }
                  style={{width: "50%"}}
                  />
                </Col>
              </Row>
              <Row>
                <Col style={{marginTop:"10px"}}>
                  <Button variant="primary" style={{marginLeft: "0px"}}
                  onClick={ this.download }>
                    Download
                  </Button>
                </Col>
              </Row>
            </Container>
        </Card.Body>
      </Card>
      </div>
    );
  }
}

export default App;
