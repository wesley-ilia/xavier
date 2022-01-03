export const getCidades = (app) => {
	const opt = [
		{label: "São Paulo", value: "São Paulo"},
		{label: "Campinas", value: "Campinas"}
	]
	app.setState({ cidades: opt } );
}