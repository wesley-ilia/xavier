import axios from "axios";
import React from "react";

export var BASE_URL = `http://${process.env.REACT_APP_BASE_URL}:8000`;

var estados_ori = [
  "AC",
  "AL",
  "AM",
  "AP",
  "BA",
  "CE",
  "DF",
  "ES",
  "GO",
  "MA",
  "MG",
  "MS",
  "MT",
  "PA",
  "PB",
  "PE",
  "PI",
  "PR",
  "RJ",
  "RN",
  "RO",
  "RR",
  "RS",
  "SC",
  "SE",
  "SP",
  "TO",
];

var i;

export default class Dropdown extends React.Component {
  constructor() {
    super();
    this.estados = [];
    this.mercados = [];
    this.stacks = [];
    this.colunas = [];
    this.getDropdown();
  }

  getDropdown = async () => {
    for (i = 0; i < estados_ori.length; i++) {
      this.estados.push({
        label: estados_ori[i],
        value: estados_ori[i],
      });
    }

    const response = await axios.get(BASE_URL + "/dropdown");
    const data = response.data;
    for (i = 0; i < data.mercados.length; i++) {
      this.mercados.push({
        label: data.mercados[i],
        value: data.mercados[i],
      });
    }

    for (i = 0; i < data.stacks.length; i++) {
      this.stacks.push({
        label: data.stacks[i],
        value: data.stacks[i],
      });
    }

    for (i = 0; i < data.colunas.length; i++) {
      this.colunas.push({
        label: data.colunas[i],
        value: data.colunas[i],
      });
    }
  };
}
