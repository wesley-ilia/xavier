import pandas as pd
import main
import os
from os.path import exists

home = os.path.expanduser('~')


def test_insert_DF_FINANCAS_GAMES_PYTHON_JAVASCRIPT_expected_csv_with_2_elements():
    try:
        os.remove(path=home + "/Downloads/output_1.csv")
    except FileNotFoundError:
        pass
    main.tester(estados=['DF'], mercados=['Finanças', 'Games'], stacks=['Python', 'JavaScript'], name='output_1')
    assert pd.read_csv(home + "/Downloads/output_1.csv").equals(pd.read_csv("assert_1.csv")) is True

def test_insert_DF_FINANCAS_expected_csv_with_10_elements():
    try:
        os.remove(path=home + "/Downloads/output_2.csv")
    except FileNotFoundError:
        pass
    main.tester(estados=['DF'], mercados=['Finanças'], stacks=[], name='output_2')
    assert len(pd.read_csv(home + "/Downloads/output_2.csv").index) == 10


def test_insert_DF_AGRONEGOCIO_expected_csv_with_8_elements():
    try:
        os.remove(path=home + "/Downloads/output_3.csv")
    except FileNotFoundError:
        pass
    main.tester(estados=['DF'], mercados=['Agronegócio'], stacks=[], name='output_3')
    assert len(pd.read_csv(home + "/Downloads/output_3.csv").index) == 8


def test_insert_DF_AND_NON_EXISTING_MARKET_expected_csv_with_0_elements():
    out_name = 'output_4'
    try:
        os.remove(path=home + "/Downloads/" + out_name + ".csv")
    except FileNotFoundError:
        pass
    main.tester(estados=['DF'], mercados=['Luiz Felipe'], stacks=[], name=out_name)
    assert len(pd.read_csv(home + "/Downloads/" + out_name + ".csv").index) == 0


def test_insert_NON_EXISTING_ESTATE_AND_MARKET_expected_csv_with_0_elements():
    out_name = 'output_5'
    try:
        os.remove(path=home + "/Downloads/" + out_name + ".csv")
    except FileNotFoundError:
        pass
    main.tester(estados=['AW'], mercados=['Agronegócio'], stacks=[], name=out_name)
    assert len(pd.read_csv(home + "/Downloads/" + out_name + ".csv").index) == 0


def test_insert_DF_AND_Agronegocio_AND_NON_EXISTING_STACK_expected_csv_with_0_elements():
    out_name = 'output_6'
    try:
        os.remove(path=home + "/Downloads/" + out_name + ".csv")
    except FileNotFoundError:
        pass
    main.tester(estados=['DF'], mercados=['Agronegócio'], stacks=['Luiz Felipe'], name=out_name)
    assert len(pd.read_csv(home + "/Downloads/" + out_name + ".csv").index) == 0


def test_insert_NOTHING_expected_no_csv():
    out_name = 'output_7'
    try:
        os.remove(path=home + "/Downloads/" + out_name + ".csv")
    except FileNotFoundError:
        pass
    main.tester(estados=[], mercados=[], stacks=[], name=out_name)
    assert exists(home + "/Downloads/" + out_name + ".csv") is False


def test_insert_EVERYTHING_WRONG_expected_csv_with_0_elements():
    out_name = 'output_9'
    try:
        os.remove(path=home + "/Downloads/" + out_name + ".csv")
    except FileNotFoundError:
        pass
    main.tester(
            estados=['DF', 'Luiz Felipe'],
            mercados=['Finanças', 'Games', 'Luiz Felipe'],
            stacks=['Python', 'JavaScript', 'Luiz Felipe'],
            name=out_name)
    assert pd.read_csv(home + "/Downloads/output_1.csv").equals(pd.read_csv("assert_1.csv")) is True
