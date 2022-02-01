
import { createGlobalStyle } from 'styled-components';
import { lightMode } from './light-mode.js';
import { darkMode } from './dark-mode.js';

export var lightColor = "#fff"
export var darkColor = "#303030"

export var GlobalStyle = createGlobalStyle`
  ${props => props.theme.mode === 'light' ? lightMode : darkMode};
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

	input: (provided, state) => ({
		...provided,
		color: lightColor,
	}),

	valueContainer: (provided, state) => ({
		...provided,
		background: darkColor,
		color: lightColor,
	}),
	multiValueLabel: (provided, state) => ({
		...provided,
		background: "grey",
		color: lightColor,
	}),
	multiValue: (provided, state) => ({
		...provided,
		background: "grey",
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
		background: darkColor,
	}),
  }
  
  export var lightGeneric = {
	background: lightColor,
	backgroundColor: lightColor,
	color: darkColor,
	border: 'solid 1px lightgrey'
  }
  
  export var darkGeneric = {
	background: darkColor,
	backgroundColor: darkColor,
	color: lightColor,
	border: 'solid 1px white'
  }