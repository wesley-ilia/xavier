import pytest
import pandas as pd
import bot_test
import numpy as np
import os

home = os.path.expanduser('~')
def test_insert_DF_FINANCAS_GAMES_PYTHON_JAVASCRIPT_expected_csv_with_2_elements():
    try:
        os.remove(path=home + "/Downloads/output_1.csv")
    except FileNotFoundError:
        pass
    bot_test.tester(estados=['DF'], mercados=['Finanças', 'Games'], stacks=['Python', 'JavaScript'], name='output_1')
    assert pd.read_csv(home + "/Downloads/output_1.csv").equals(pd.read_csv("assert_1.csv")) == True

def test_insert_DF_FINANCAS_expected_csv_with_10_elements():
    try:
        os.remove(path=home + "/Downloads/output_2.csv")
    except FileNotFoundError:
        pass
    bot_test.tester(estados=['DF'], mercados=['Finanças'], stacks=[], name='output_2')
    assert len(pd.read_csv(home + "/Downloads/output_2.csv").index) == 10

def test_insert_DF_AGRONEGOCIO_expected_csv_with_8_elements():
    try:
        os.remove(path=home + "/Downloads/output_3.csv")
    except FileNotFoundError:
        pass
    bot_test.tester(estados=['DF'], mercados=['Agronegócio'], stacks=[], name='output_3')
    assert len(pd.read_csv(home + "/Downloads/output_3.csv").index) == 8

def test_insert_DF_NON_EXISTANT_MARKET_expected_csv_with_0_elements():
    out_name = 'output_4'
    try:
        os.remove(path=home + "/Downloads/" + out_name + "csv")
    except FileNotFoundError:
        pass
    bot_test.tester(estados=['DF'], mercados=['Luiz Felipe'], stacks=[], name=out_name)
    assert len(pd.read_csv(home + "/Downloads/" + out_name + ".csv").index) == 0