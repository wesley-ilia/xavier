import React from 'react';
import Select from 'react-select';
import { Button } from 'react-native';

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
    this.preview = '0';
    this.estados = [];
    this.mercados = [];
    this.stacks = [];
    this.state = {
      preview: "0",
    }
    this.fileName = "Untitled.csv";
    this.getDropdown()
  }

  getDropdown = async () => {
    const req_options = {
      method: "GET",
    }
    const response = await fetch("/dropdown", req_options);
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
    await fetch("/search?get_csv=true&market="+this.mercadosExecute
    +"&stack="+this.stacksExecute+"&state="+this.estadosExecute, req_options)
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
        this.fileName,
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
    const response = await fetch("/search?get_csv=false&market="+this.mercadosExecute
    +"&stack="+this.stacksExecute+"&state="+this.estadosExecute, req_options);
    
    const data = response.json();
    var that = this;
    data.then(function(resp) {
      that.setState({preview: resp});
    })
  };

  handleChangeEstados = e => {
    var values = [];
    for (i = 0; i < e.length; i++)
      values.push(e[i].value);
    this.estadosExecute = [...values];
    this.getPreview();
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
      this.fileName = "Untitled.csv";
    else
      this.fileName = e.target.value + ".csv";
  }

  /* useEffect(() => {
    getDropdown();
  }, []) */
  render () {
    return (
      <div className="App">
        <div className='estados'>
        <h2 className="category-title">Estados</h2>
          <Select
          options={this.estados}
          isMulti
          onChange={ this.handleChangeEstados }
        />
        </div>
        <div className='mercados'>
        <h2 className="category-title">Mercados</h2>
          <Select
          options={this.mercados}
          isMulti
          onChange={ this.handleChangeMercados }
        />
        </div>
        <div className='estados'>
        <h2 className="category-title">Stacks</h2>
          <Select
          options={this.stacks}
          isMulti
          onChange={ this.handleChangeStacks }
        />
        </div>
        <div>
          <h3 className="input-header">Nome do arquivo</h3>
          <input
          type="text" id="file_name"
          onChange={ this.handleChangeFile }
          />
          <span>
           .csv
          </span>
        </div>
        {this.preview && <div style={{ marginTop: 20, lineHeight: '25px' }}>
          <div>Preview: { this.state.preview }</div>
        </div>}
        <Button
        title='Download'
        onPress={ this.download }
        />
      </div>
    );
  }
}

export default App;
