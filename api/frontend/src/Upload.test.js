import Upload from './Upload';
import { render, screen, cleanup, fireEvent } from '@testing-library/react';
import React from 'react';
import selectEvent from 'react-select-event'
import { act } from 'react-dom/test-utils';

afterEach(cleanup);

test('render upload button', () => {
  render(<Upload/>);
  expect(screen.getByTestId("fazer-upload")).toBeTruthy();
});

test('description when the mouse is over', async () => {
  await act(async () => {
    render(<Upload/>);
    await fireEvent.mouseOver(screen.getByTestId("downloadModelo"))
    expect(screen.getByTestId("modelo-descricao")).toBeTruthy();
  });
});

test('user-description when the mouse is over', async () => {
  await act(async () => {
    render(<Upload/>);
    await fireEvent.mouseOver(screen.getByTestId("downloadUsuario"))
    expect(screen.getByTestId("usuario-descricao")).toBeTruthy();
  });
});