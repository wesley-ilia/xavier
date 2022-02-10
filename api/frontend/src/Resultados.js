import React from "react";
import Container from "react-bootstrap/esm/Container";
import Select from "react-select";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Dropdown from "./Dropdown";
import { analytics } from '.';
import { logEvent } from 'firebase/analytics';

class Resultados extends React.Component {
  constructor() {
    super();
    this.state = {
      theme,
    };
    this.dropdown = new Dropdown();
  }

  render() {
    return (
      <Container>
        <Row>
          <Col>
            <form data-testid="form-colunas">
              <label htmlFor="colunas">
                <h2>Colunas</h2>
              </label>
              <Select
                styles={this.props.theme === "light" ? lightSelect : darkSelect}
                defaultValue={[
                  { label: "nome", value: "nome" },
                  { label: "estado", value: "estado" },
                  { label: "cidade", value: "cidade" },
                  { label: "mercado", value: "mercado" },
                  { label: "stacks", value: "stacks" },
                ]}
                classNamePrefix="colunas"
                name="colunas"
                inputId="colunas"
                options={this.dropdown.colunas}
                isMulti
                onChange={this.handleChangeColunas}
              />
            </form>
          </Col>
        </Row>
        <Row>
          <Col>
            <div
              id="preview"
              style={{ marginTop: "10px", marginBottom: "10px" }}
            >
              <label htmlFor="previer">
                <h5>Preview: {this.state.preview} </h5>
              </label>
            </div>
          </Col>
        </Row>
        <Row>
          <Col>Nome do arquivo</Col>
        </Row>
        <Row>
          <Col xs lg="7">
            <Form.Control
              name="teste"
              placeholder="Nome do arquivo"
              onChange={this.handleChangeFile}
              style={this.props.theme === "light" ? lightGeneric : darkGeneric}
            />
          </Col>
          <Col xs lg="4">
            <form data-testid="file-Type">
              <label hidden data-testid="label-type" htmlFor="fileType">
                type
              </label>
              <Select
                styles={this.props.theme === "light" ? lightSelect : darkSelect}
                classNamePrefix="fileType"
                name="fileType"
                inputId="fileType"
                options={[
                  { label: "Excel", value: "xlsx" },
                  { label: "CSV", value: "csv" },
                  { label: "PDF", value: "pdf" },
                ]}
                defaultValue={{ label: "Excel", value: "xlsx" }}
                onChange={this.handleChangeExtension}
                style={{ width: "50%" }}
              />
            </form>
          </Col>
        </Row>
        <Row>
          <Col style={{ marginTop: "10px" }}>
            <Button
              className={
                this.props.theme === "light" ? "btn-primary" : "btn-info"
              }
              data-testid="download"
              variant="primary"
              style={{ marginLeft: "0px" }}
              onClick={this.download}
            >
              Download
            </Button>
          </Col>
        </Row>
        <Row>
          <Col style={{ paddingTop: "10px" }}>
            <Button
              className={
                this.props.theme === "light" ? "btn-primary" : "btn-info"
              }
              data-testid="upload"
              variant="primary"
              onClick={this.upload}
            >
              Upload...
            </Button>
          </Col>
        </Row>
      </Container>
    );
  }
}

export default Resultados;
