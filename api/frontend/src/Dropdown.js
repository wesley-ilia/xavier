import React from 'react';

export var BASE_URL = "http://localhost:8000"

var estados_ori = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO'];

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
        value: estados_ori[i]
      });
    }

    const req_options = {
      method: "GET",
    }
    const response = await fetch(BASE_URL + "/dropdown", req_options);
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

      for (i = 0; i < resp.colunas.length; i++) {
        that.colunas.push({
          label: resp.colunas[i],
          value: resp.colunas[i]
        });
      }
    })
  };
}