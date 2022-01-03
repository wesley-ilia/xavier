import App from './App';
import Dropdown from './Dropdown';
import { render, screen, cleanup, fireEvent } from '@testing-library/react';
import React from 'react';
import selectEvent from 'react-select-event'
import { act } from 'react-dom/test-utils';
jest.mock('./Dropdown');

afterEach(cleanup);

test('renders Card', () => {
  const { getByTestId } = render(<App/>);
  const card = getByTestId("card");
  expect(card).toBeTruthy();
});

test('renders form estados', () => {
  const { getByTestId } = render(<App/>);
  const form_estados = getByTestId("form-estados");
  expect(form_estados).toBeTruthy();
});

test('select [DF, SP] from estados dropdown', async () => {
  const { getByTestId, getByLabelText } = render(<App/>);

  await selectEvent.select(getByLabelText('Estados'), ['DF', 'SP']);

  expect(getByTestId('form-estados')).toHaveFormValues({estados: ['DF', 'SP']})

});

test('renders form mercados', () => {
  const { getByTestId } = render(<App/>);
  const form_mercados = getByTestId("form-mercados");
  expect(form_mercados).toBeTruthy();
});

test('Dropdown mock works', () => {
  var drop = new Dropdown();
  expect(drop.mercados).toBeTruthy();
});

test('check nothing in mercados dropdown', async () => {
  render(<App/>);
  
  expect(screen.getByTestId('form-mercados')).toHaveFormValues({mercados: ''})
});

test('select Finanças from mercados dropdown', async () => {
    render(<App/>);
    
    await selectEvent.select(screen.getByLabelText('Mercados'), ['Finanças']);

    expect(screen.getByTestId('form-mercados')).toHaveFormValues({mercados: 'Finanças'})
});

test('renders form stacks', () => {
  render(<App/>);
  const form_stacks = screen.getByTestId("form-stacks");
  expect(form_stacks).toBeTruthy();
});

test('check nothing in stacks dropdown', async () => {
  render(<App/>);
  
  expect(screen.getByTestId('form-stacks')).toHaveFormValues({stacks: ''})
});

test('select C++ and C# from stacks dropdown', async () => {
  render(<App/>);
  
  await selectEvent.select(screen.getByLabelText('Stacks'), ['C++', 'C#']);

  expect(screen.getByTestId('form-stacks')).toHaveFormValues({stacks: ['C++', 'C#']})
});

test('check if cidades does not render before especificas clicked', () => {
  render(<App/>);
  expect(screen.queryByTestId("form-cidades")).toBeFalsy();
});

test('check if cidades render when especificas clicked', async () => {
  await act(async () => {
    render(<App/>);
    const radio = screen.getAllByRole('radio');
    await fireEvent.click(radio[2]);

    expect(screen.getByTestId("form-cidades")).toBeTruthy();
  });
});
