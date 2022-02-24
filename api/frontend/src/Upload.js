import axios from "axios";
import { BASE_URL } from "./Dropdown";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import Table from "react-bootstrap/Table";
import modelo from "./modelo.csv";
import Spinner from "react-bootstrap/Spinner";
import React, { Component } from "react";
import { lightGeneric } from "./themes";
import { analytics } from "./App";
import { logEvent } from "firebase/analytics";

class Upload extends Component {
  constructor() {
    super();
    this.state = {
      redirect: "",
      isLoading: false,
      isDownloading: false,
      val: 0,
      progress: 0,
      message: "",
      selectedFile: null,
    };
  }

  // On file select (from the pop up)
  onFileChange = (event) => {
    // Update the state
    this.setState({ selectedFile: event.target.files[0] });
  };

  onFileUpload = async () => {
    let analyticsHere = await analytics;
    if (this.state.selectedFile === null) {
      alert("Por favor, selecione algum arquivo");
      if (analyticsHere !== "Error") {
        logEvent(analyticsHere, "upload", {
          error: true,
          message: "sem_arquivo",
        });
      }
      return;
    }
    const extension = this.state.selectedFile.name.slice(-4);
    if (extension !== ".csv") {
      alert("Por favor, selecione um arquivo CSV");
      if (analyticsHere !== "Error") {
        logEvent(analyticsHere, "upload", {
          error: true,
          message: "non_csv",
        });
      }
      return;
    }

    this.setState({ isLoading: true, val: 0 });
    let currentFile = this.state.selectedFile;

    let formData = new FormData();

    formData.append("file", currentFile);

    const response = await axios.post(BASE_URL + "/api/uploadfile", formData);
    let error = false;
    let message;
    try {
      if (response.data.message.includes("faltando")) {
        error = true;
        message = "sem_nome";
      } else message = "sucesso";
      this.setState({ isLoading: false, val: 100 });
    } catch (e) {
      this.setState({ isLoading: false, val: 100 });
      alert("Erro ao fazer upload");
      error = true;
      message = "problema_interno";
    }
    if (analyticsHere !== "Error") {
      logEvent(analyticsHere, "upload", {
        error: error,
        message: message,
      });
    }
  };

  downloadModelo = async () => {
    let analyticsHere = await analytics;
    if (analyticsHere !== "Error") {
      logEvent(analyticsHere, "download_modelo", {});
    }
    const link = document.createElement("a");
    link.href = modelo;
    link.setAttribute("download", "modelo.csv");

    // Append to html link element page
    document.body.appendChild(link);

    // Start download
    link.click();

    // Clean up and remove the link
    link.parentNode.removeChild(link);
  };

  downloadTabelaUsuario = async () => {
    let analyticsHere = await analytics;
    this.setState({ isDownloading: true, val: 0 });

    axios
      .get(BASE_URL + "/api/download-user-table")
      .then((response) => response.blob())
      .then((blob) => {
        // Create blob link to download
        const url = window.URL.createObjectURL(new Blob([blob]));
        const link = document.createElement("a");
        link.href = url;
        link.setAttribute("download", "tabela_usuario.csv");

        // Append to html link element page
        document.body.appendChild(link);

        // Start download
        link.click();

        // Clean up and remove the link
        link.parentNode.removeChild(link);
        this.setState({ isDownloading: false, val: 100 });
        if (analyticsHere !== "Error") {
          logEvent(analyticsHere, "download_usuario", {
            error: false,
          });
        }
      })
      .catch((error) => {
        alert("Ocorreu um problema com o Download");
        if (analyticsHere !== "Error") {
          logEvent(analyticsHere, "download_usuario", {
            error: true,
          });
        }
      });
  };

  voltar = () => {
    this.setState({ redirect: "/" });
  };

  render() {
    return (
      <div className="upload-wrapper">
        <div className="upload-sections">
          <center>
            <h3>ADICIONE DADOS</h3>
          </center>
        </div>
        <div className="upload-sections">
          <Table striped bordered hover>
            <thead>
              <tr>
                <th>nome</th>
                <th>estado</th>
                <th>cidade</th>
                <th>mercado</th>
                <th>stacks</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <th>Xavier</th>
                <th>SP</th>
                <th>São Paulo</th>
                <th>TI</th>
                <th>Python</th>
              </tr>
            </tbody>
          </Table>
        </div>
        <div className="upload-sections">
          <Button
            className={
              this.props.theme === "light" ? "btn-primary" : "btn-info"
            }
            style={{ width: "100%" }}
            data-testid="downloadModelo"
            variant="primary"
            onClick={this.downloadModelo}
          >
            Baixar Modelo
          </Button>
        </div>
        <div className="upload-sections">
          <Form.Control
            type="file"
            style={lightGeneric}
            onChange={this.onFileChange}
          />
          <Button
            style={{ width: "100%" }}
            className={
              this.props.theme === "light" ? "btn-primary" : "btn-info"
            }
            data-testid="upload"
            variant="primary"
            onClick={this.onFileUpload}
          >
            {this.state.isLoading && (
              <Spinner
                as="span"
                animation="grow"
                size="sm"
                role="status"
                aria-hidden="true"
              />
            )}
            Upload!
          </Button>
        </div>
        <div className="upload-sections">
          <Button
            className={
              this.props.theme === "light" ? "btn-primary" : "btn-info"
            }
            style={{ width: "100%" }}
            data-tip="React-tootltip"
            data-testid="downloadUsuario"
            variant="primary"
            onClick={this.downloadTabelaUsuario}
          >
            {this.state.isDownloading && (
              <Spinner
                as="span"
                animation="grow"
                size="sm"
                role="status"
                aria-hidden="true"
              />
            )}
            Tabela do Usuário
          </Button>
          <center>Tabela com todos os dados personalizados</center>
        </div>
      </div>
    );
  }
}

export default Upload;
