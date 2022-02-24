import React from "react";
import Select from "react-select";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import Dropdown, { BASE_URL } from "./Dropdown";
import "bootstrap/dist/css/bootstrap.min.css";
import { getCidades } from "./Utils";
import { darkSelect, lightSelect, lightGeneric } from "./themes";
import { analytics } from "./App";
import { logEvent } from "firebase/analytics";
import Card from "react-bootstrap/Card";
import Upload from "./Upload";
import { ThemeProvider } from "styled-components";
import { GlobalStyle } from "./themes";
import "./consulta.css";
import axios from "axios";

var i;

class Consulta extends React.Component {
  constructor() {
    super();
    this.selectRef = null;
    this.estadosExecute = [];
    this.mercadosExecute = [];
    this.stacksExecute = [];
    this.cidadesExecute = [];
    this.colunasExecute = ["nome", "estado", "cidade", "mercado", "stacks"];
    this.capitais = "esp";
    this.state = {
      redirect: "",
      preview: "0",
      cidades: [],
      showCidades: true,
    };
    this.fileName = "Untitled";
    this.extension = "xlsx";
    this.dropdown = new Dropdown();
    this.flexStyle = {
      // flex: "1 1 414px",
      width: "414px",
      margin: "10px",
      // marginLeft: "10px",
      // marginRight: "10px",
    };
  }

  download = async () => {
    let analyticsHere = await analytics;
    /* log event to firebase */
    if (analyticsHere !== "Error") {
      logEvent(analyticsHere, "download", {
        estados: this.estadosExecute,
        capitais: this.capitais,
        cidades: this.cidadesExecute,
        mercados: this.mercadosExecute,
        stacks: this.stacksExecute,
        preview: this.state.preview,
        extension: this.extension,
        colunas: this.colunasExecute,
      });
    }

    if (
      this.mercadosExecute.length === 0 &&
      this.estadosExecute.length === 0 &&
      this.stacksExecute.length === 0
    ) {
      alert("Preencha algum campo");
      return;
    }
    await fetch(
      BASE_URL +
        "/search?market=" +
        this.mercadosExecute +
        "&stack=" +
        this.stacksExecute +
        "&state=" +
        this.estadosExecute +
        "&extension=" +
        this.extension +
        "&cidade=" +
        this.cidadesExecute +
        "&capitais=" +
        this.capitais +
        "&colunas=" +
        this.colunasExecute,
      { method: "GET" }
    )
      .then((response) => response.blob())
      .then((blob) => {
        // Create blob link to download
        const url = window.URL.createObjectURL(new Blob([blob]));
        const link = document.createElement("a");
        link.href = url;
        link.setAttribute("download", this.fileName + "." + this.extension);

        // Append to html link element page
        document.body.appendChild(link);

        // Start download
        link.click();

        // Clean up and remove the link
        link.parentNode.removeChild(link);
      });
  };

  getPreview = async () => {
    const response = await axios.get(
      BASE_URL +
        "/preview?market=" +
        this.mercadosExecute +
        "&stack=" +
        this.stacksExecute +
        "&state=" +
        this.estadosExecute +
        "&cidade=" +
        this.cidadesExecute +
        "&capitais=" +
        this.capitais
    );

    const data = await response.data;
    this.setState({ preview: data });
  };

  handleChangeEstados = async (e) => {
    // logEvent(analytics, 'goal_completion', { name: 'lever_puzzle'})
    /* log event to firebase */
    let analyticsHere = await analytics;
    if (analyticsHere !== "Error") {
      logEvent(analyticsHere, "select_content", {
        content_type: "dropdown_selection",
        content_id: "select_estados",
      });
    }
    var values = [];
    for (i = 0; i < e.length; i++) values.push(e[i].value);
    this.estadosExecute = [...values];
    this.getPreview();
    if (this.state.showCidades) getCidades(this);
  };

  handleChangeCidades = (e) => {
    var values = [];
    for (i = 0; i < e.length; i++) values.push(e[i].value);
    this.cidadesExecute = [...values];
    this.getPreview();
  };

  handleChangeMercados = async (e) => {
    /* log event to firebase */
    let analyticsHere = await analytics;
    if (analyticsHere !== "Error") {
      logEvent(analyticsHere, "select_content", {
        content_type: "dropdown_selection",
        content_id: "select_mercados",
      });
    }
    var values = [];
    for (i = 0; i < e.length; i++) values.push(e[i].value);
    this.mercadosExecute = [...values];
    this.getPreview();
  };

  handleChangeColunas = (e) => {
    var values = [];
    for (i = 0; i < e.length; i++) values.push(e[i].value);
    this.colunasExecute = [...values];
  };

  handleChangeStacks = async (e) => {
    /* log event to firebase */
    let analyticsHere = await analytics;
    if (analyticsHere !== "Error") {
      logEvent(analyticsHere, "select_content", {
        content_type: "dropdown_selection",
        content_id: "select_stacks",
      });
    }
    var values = [];
    for (i = 0; i < e.length; i++)
      values.push(e[i].value.replace("c++", "cpp").replace("c#", "csharp"));
    this.stacksExecute = [...values];
    this.getPreview();
  };

  handleChangeFile = (e) => {
    if (e.target.value === "") this.fileName = "Untitled";
    else this.fileName = e.target.value;
  };

  handleChangeExtension = (e) => {
    this.extension = e.value;
  };

  clearCidades = () => {
    this.cidadesExecute = this.cidadesExecute.reduce(() => []);
    this.selectRef.clearValue();
  };

  handleCidadesCheck = (e) => {
    if (e.target.checked) {
      this.capitais = "nao";
      this.getPreview();
      this.setState({ showCidades: false });
      this.clearCidades();
    } else {
      this.capitais = "esp";
      this.getPreview();
      this.setState({ showCidades: true });
    }
  };

  upload = () => {
    this.setState({ redirect: "/upload" });
  };

  Pesquisa = () => {
    return (
      <Card style={this.flexStyle}>
        <Card.Body>
          <div className="sections">
            <form data-testid="form-estados">
              <label htmlFor="estados">
                <h3>Estados</h3>
              </label>
              <Select
                styles={this.props.theme === "light" ? lightSelect : darkSelect}
                classNamePrefix="estados"
                name="estados"
                inputId="estados"
                options={this.dropdown.estados}
                isMulti
                onChange={this.handleChangeEstados}
              />
            </form>
          </div>
          <div className="sections">
            <form data-testid="form-cidades">
              <div style={{ display: "flex" }}>
                <label htmlFor="cidades" style={{ flex: "1 1 auto" }}>
                  <h3>Cidades</h3>
                </label>
                <div style={{ flex: "1 1 auto" }}>
                  <input
                    type="checkbox"
                    id="sem"
                    value="nao"
                    onChange={this.handleCidadesCheck}
                  />{" "}
                  Sem Capitais
                </div>
              </div>
              <Select
                ref={(ref) => {
                  this.selectRef = ref;
                }}
                isDisabled={!this.state.showCidades}
                styles={this.props.theme === "light" ? lightSelect : darkSelect}
                classNamePrefix="cidades"
                name="cidades"
                inputId="cidades"
                options={this.state.cidades}
                isMulti
                onChange={this.handleChangeCidades}
              />
            </form>
          </div>
          <div className="sections">
            <form data-testid="form-mercados">
              <label htmlFor="mercados">
                <h3>Mercados</h3>
              </label>
              <Select
                styles={this.props.theme === "light" ? lightSelect : darkSelect}
                classNamePrefix="mercados"
                name="mercados"
                inputId="mercados"
                options={this.dropdown.mercados}
                isMulti
                onChange={this.handleChangeMercados}
              />
            </form>
          </div>
          <div className="sections">
            <form data-testid="form-stacks">
              <label htmlFor="stacks">
                <h3>Stacks</h3>
              </label>
              <Select
                styles={this.props.theme === "light" ? lightSelect : darkSelect}
                classNamePrefix="stacks"
                name="stacks"
                inputId="stacks"
                options={this.dropdown.stacks}
                isMulti
                onChange={this.handleChangeStacks}
              />
            </form>
          </div>
        </Card.Body>
      </Card>
    );
  };

  Resultados = () => {
    return (
      <Card style={this.flexStyle}>
        <Card.Body>
          <div className="sections" id="preview">
            <label htmlFor="preview">
              <h3>Resultados:</h3>
              <h2>{this.state.preview}</h2>
            </label>
          </div>
          <div className="sections">
            <form data-testid="form-colunas">
              <label htmlFor="colunas">
                <h3>Colunas</h3>
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
          </div>
          <div className="sections">
            <h3>Nome</h3>
            <div style={{ display: "flex" }}>
              <Form.Control
                name="teste"
                placeholder="Nome do arquivo"
                onChange={this.handleChangeFile}
                style={Object.assign({}, lightGeneric, { flex: 1 })}
              />
              <form data-testid="file-Type">
                {/* <label hidden data-testid="label-type" htmlFor="fileType">
                  type
                </label> */}
                <Select
                  styles={
                    this.props.theme === "light" ? lightSelect : darkSelect
                  }
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
                />
              </form>
            </div>
          </div>
          <Button
            className={
              this.props.theme === "light" ? "btn-primary" : "btn-info"
            }
            data-testid="download"
            variant="primary"
            style={{ width: "100%" }}
            onClick={this.download}
          >
            Download
          </Button>
        </Card.Body>
      </Card>
    );
  };

  Upload = () => {
    return (
      <Card style={this.flexStyle}>
        <Card.Body>
          <Upload theme={this.props.theme} />
        </Card.Body>
      </Card>
    );
  };

  render() {
    return (
      <div
        style={{
          display: "flex",
          flexWrap: "wrap",
          // gap: "10px",
          justifyContent: "center",
        }}
      >
        <ThemeProvider theme={{ mode: this.props.theme }}>
          <>
            <GlobalStyle />
            <this.Pesquisa />
            <this.Resultados />
            <this.Upload />
          </>
        </ThemeProvider>
      </div>
    );
  }
}

export default Consulta;
