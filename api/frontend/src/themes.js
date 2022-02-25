import { createGlobalStyle } from "styled-components";
import { lightMode } from "./light-mode.js";
import { darkMode } from "./dark-mode.js";

export var lightColor = "#fff";
export var darkColor = "#202020";

export var GlobalStyle = createGlobalStyle`
  ${(props) => (props.theme.mode === "light" ? lightMode : darkMode)};
`;

export var lightSelect = {
  menu: (provided, state) => ({
    ...provided,
    background: lightColor,
    color: darkColor,
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
};

export var darkSelect = {
  menu: (provided, state) => ({
    ...provided,
    background: darkColor,
    color: lightColor,
  }),

  input: (provided, state) => ({
    ...provided,
    color: darkColor,
  }),

  valueContainer: (provided, state) => ({
    ...provided,
    background: lightColor,
    color: darkColor,
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
    background: lightColor,
    color: darkColor,
  }),
  singleValue: (provided, state) => ({
    ...provided,
    background: lightColor,
    color: darkColor,
  }),
  option: (provided, state) => ({
    ...provided,
    backgroundColor: state.isFocused ? "grey" : null,
    color: lightColor,
  }),
  control: (provided, state) => ({
    ...provided,
    color: "red",
    background: lightColor,
  }),
};

export var lightGeneric = {
  background: lightColor,
  backgroundColor: lightColor,
  color: darkColor,
  border: "solid 1px lightgrey",
};

export var darkGeneric = {
  background: darkColor,
  backgroundColor: darkColor,
  color: lightColor,
  border: "solid 1px white",
};
