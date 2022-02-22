from pandas import DataFrame, read_parquet
from unidecode import unidecode

estados_dict = {
    "acre": "ac",
    "alagoas": "al",
    "amapa": "ap",
    "amazonas": "am",
    "bahia": "ba",
    "ceara": "ce",
    "distrito federal": "df",
    "espirito santo": "es",
    "goias": "go",
    "maranhao": "ma",
    "mato grosso": "mt",
    "mato grosso do sul": "ms",
    "minas gerais": "mg",
    "para": "pa",
    "paraiba": "pb",
    "parana": "pr",
    "pernambuco": "pe",
    "piaui": "pi",
    "rio de janeiro": "rj",
    "rio grande do norte": "rn",
    "rio grande do sul": "rs",
    "rondonia": "ro",
    "roraima": "rr",
    "santa catarina": "sc",
    "sao paulo": "sp",
    "sergipe": "se",
    "tocantins": "to"
}


def narray_colunm_to_list(column):
    for i in range(len(column)):
        column[i] = column[i].tolist()


def format_to_ascii_characters(df: DataFrame, column):
    df[column] = [unidecode(
        string.lower().strip()) for string in df[column].values]


def make_column_state(df: DataFrame):
    df['estado'] = df['contato']
    for i, contato in enumerate(df['contato']):
        contato = unidecode(contato.split(',')[-2].lower().strip())
        if contato in estados_dict.keys():
            df['estado'][i] = estados_dict[contato]
        else:
            df['estado'][i] = contato


def codesh_normalize():
    df = read_parquet('./raw_data/codesh.parquet')

    narray_colunm_to_list(df['stacks'])
    narray_colunm_to_list(df['redes'])

    df['name'] = df['name'].str.lower().str.strip()

    for i, lst in enumerate(df['stacks']):
        df['stacks'][i] = [unidecode(
            string.lower().strip()) for string in df['stacks'][i]]

    for column in filter(
            lambda x: x not in {'name', 'stacks', 'redes'}, df.columns):
        format_to_ascii_characters(df, column)

    make_column_state(df)

    df.to_parquet("./clean_data/codesh.parquet", index=False)
