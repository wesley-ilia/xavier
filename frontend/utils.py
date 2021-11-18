import pandas
from Log import Log


def make_csv(query: str, name_csv: str, connection_db: object) -> bool:
    results = pandas.read_sql_query(query, connection_db)
    error = False
    if results.empty:
        error = True
    results.to_csv(name_csv, index=False)
    return error


def insert_log_in_db(db: Log, query: str, obs: str,
                     output_csv: str = "untitled.csv"):
    version = "0.0.1"
    df = pandas.read_csv(output_csv)
    result_csv = str(df.to_csv(header=False, index=False)).replace('\'', '')

    query = query.replace('\'', '')
    db.insert_into_log(query, version, result_csv, obs)
