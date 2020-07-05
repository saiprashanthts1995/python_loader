from mysql import connector as mc
import datetime
import json
import pandas as pd


def mysql_connection(env):
    pass


def postgres_connection(env):
    pass


def read_config(env, database_type):
    with open('config.json') as config_file:
        config_file_content = json.load(config_file)
    return config_file_content[env.upper()][database_type.upper()]


def tables_to_be_loaded():
    table_df = pd.read_csv('tables_to_loaded.txt', sep=':')
    table_df = table_df.query("to_be_loaded == 'yes'")
    return table_df['table_name'].to_list()


def time(method):
    def time_method(*args, **kwargs):
        ts = datetime.datetime.now()
        result = method(*args, **kwargs)
        te = datetime.datetime.now()
        modern_printer('Total time took is {}'.format(te-ts))
        return result
    return time_method


def modern_printer(message):
    print('=' * 100)
    print('{}'.format(message))
    print('=' * 100)


if __name__ == '__main__':
    # print(read_config('QA', 'POSTGRES'))
    print(tables_to_be_loaded())