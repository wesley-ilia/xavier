import { createGlobalStyle } from 'styled-components';

const lightColor = "#EEE"
const darkColor = "#111"

export var GlobalStyle = createGlobalStyle`
body {
  background-color: ${props =>
    props.theme.mode === 'light' ? lightColor : darkColor};
  color: ${props =>
    props.theme.mode === 'light' ? darkColor : lightColor};
};

.card {
  background-color: ${props =>
    props.theme.mode === 'light' ? lightColor : darkColor};
  color: ${props =>
      props.theme.mode === 'light' ? darkColor : lightColor};
};
`;

export var lightSelect = {
	menu: (provided, state) => ({
	  ...provided,
	  background: lightColor,
	  color: darkColor,
	  padding: 20,
	}),
	option: (provided, state) => ({
	  ...provided,
	  backgroundColor: state.isFocused ? "lightblue" : null,
	  color: darkColor,
	}),
	control: (provided, state) => ({
	  ...provided,
	  background: lightColor,
	}),
}
  
export var darkSelect = {
	menu: (provided, state) => ({
		...provided,
		background: darkColor,
		color: lightColor,
		padding: 20,
	}),
	valueContainer: (provided, state) => ({
		...provided,
		background: darkColor,
		color: 'red',
	}),
	multiValueLabel: (provided, state) => ({
		...provided,
		background: darkColor,
		color: lightColor,
	}),
	multiValue: (provided, state) => ({
		...provided,
		background: darkColor,
		color: lightColor,
	}),
	singleValueLabel: (provided, state) => ({
		...provided,
		background: darkColor,
		color: lightColor,
	}),
	singleValue: (provided, state) => ({
		...provided,
		background: darkColor,
		color: lightColor,
	}),
	option: (provided, state) => ({
		...provided,
		backgroundColor: state.isFocused ? "grey" : null,
		color: lightColor,
	}),
	control: (provided, state) => ({
		...provided,
		color: 'red',
		background: darkColor
	}),
  }
  
  export var lightGeneric = {
	background: lightColor,
	color: darkColor,
	// border: '2px solid blue'
  }
  
  export var darkGeneric = {
	background: darkColor,
	color: lightColor,
	// border: '2px solid black'
  }