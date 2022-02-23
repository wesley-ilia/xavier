import App from "./App";
import Dropdown from "./Dropdown";
import { render, screen, cleanup, fireEvent } from "@testing-library/react";
import React from "react";
import selectEvent from "react-select-event";
import { getCidades } from "./Utils";
import { act } from "react-dom/test-utils";
import axios from "axios";

jest.mock("axios");
jest.mock("firebase/analytics");
jest.mock("./firebase");
jest.mock("./Dropdown");
jest.mock("./Utils");

afterEach(cleanup);

test("renders form estados", () => {
  const { getByTestId } = render(<App />);
  const form_estados = getByTestId("form-estados");
  expect(form_estados).toBeTruthy();
});

test("select [DF, SP] from estados dropdown", async () => {
  const { getByTestId, getByLabelText } = render(<App />);

  await selectEvent.select(getByLabelText("Estados"), ["DF", "SP"]);

  expect(getByTestId("form-estados")).toHaveFormValues({
    estados: ["DF", "SP"],
  });
});

test("renders form mercados", () => {
  const { getByTestId } = render(<App />);
  const form_mercados = getByTestId("form-mercados");
  expect(form_mercados).toBeTruthy();
});

test("Dropdown mock works", () => {
  var drop = new Dropdown();
  expect(drop.mercados).toBeTruthy();
});

test("check nothing in mercados dropdown", async () => {
  render(<App />);

  expect(screen.getByTestId("form-mercados")).toHaveFormValues({
    mercados: "",
  });
});

test("select Finanças from mercados dropdown", async () => {
  render(<App />);

  await selectEvent.select(screen.getByLabelText("Mercados"), ["Finanças"]);

  expect(screen.getByTestId("form-mercados")).toHaveFormValues({
    mercados: "Finanças",
  });
});

test("renders form stacks", () => {
  render(<App />);
  const form_stacks = screen.getByTestId("form-stacks");
  expect(form_stacks).toBeTruthy();
});

test("check nothing in stacks dropdown", async () => {
  render(<App />);

  expect(screen.getByTestId("form-stacks")).toHaveFormValues({ stacks: "" });
});

test("select C++ and C# from stacks dropdown", async () => {
  render(<App />);

  await selectEvent.select(screen.getByLabelText("Stacks"), ["C++", "C#"]);

  expect(screen.getByTestId("form-stacks")).toHaveFormValues({
    stacks: ["C++", "C#"],
  });
});

test("select file type from ... dropdown", async () => {
  await act(async () => {
    render(<App />);
    await selectEvent.select(screen.getByTestId("file-Type"), ["Excel"]);
    expect(screen.getByTestId("file-Type")).toHaveFormValues({
      fileType: "xlsx",
    });
  });
});

test("expect download to render", () => {
  render(<App />);

  const download = screen.getByTestId("download");

  expect(download).toBeTruthy();
});

test("render upload button", () => {
  render(<App />);
  expect(screen.getByTestId("upload")).toBeTruthy();
});
