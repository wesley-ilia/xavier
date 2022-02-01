import { BASE_URL } from './Dropdown'

var i;

export const getCidades = async (app) => {
  if (app.estadosExecute.length === 0) {
    app.setState({cidades: []});
    return;
  }
  console.log("teste")
	const req_options = {
	  method: "GET",
	}
	const response = await fetch(BASE_URL + "/cidades?state="
	+app.estadosExecute, req_options);
	const data = await response.json();
	var opt = []
	for (i = 0; i < data.length; i++) {
	  opt.push({ label: data[i], value: data[i] })
	}
	app.setState({ cidades: opt } );
}
