from mysql import connector as mc
import datetime
import json
import pandas as pd
import psycopg2
from loguru import logger
from sqlalchemy import create_engine


def mysql_connection(env):
    try:
        config_details = read_config(env, 'MYSQL')
        connection = mc.connect(**config_details)
        logger.info('Connection to MYSQL is successful')
        return connection
    except Exception as e:
        logger.exception('Issue in Mysql Connection Module')


def postgres_connection(env):
    try:
        config_details = read_config(env, 'POSTGRES')
        connection = psycopg2.connect(**config_details)
        logger.info('Connection to POSTGRES is successful')
        return connection
    except Exception as e:
        logger.exception('Issue in Postgres Connection Module')


def read_config(env, database_type):
    try:
        with open('config.json') as config_file:
            config_file_content = json.load(config_file)
        logger.info('Read the config details module Successfully for the following arguments env {}  database type {}'.
                    format(env, database_type))
        return config_file_content[env.upper()][database_type.upper()]
    except Exception as e:
        logger.exception('Issue in the config details module for the following arguments env {}  database type {}'.
                    format(env, database_type))


def tables_to_be_loaded():
    try:
        table_df = pd.read_csv('tables_to_loaded.txt', sep=':')
        table_df = table_df.query("to_be_loaded == 'yes'")
        logger.info('tables_to_be_loaded module ran successfully. '
                    'The list of tables to be loaded as follows {}'.format(table_df['table_name'].to_list()))
        return table_df['table_name'].to_list()
    except Exception as e:
        logger.exception('Issue in the tables_to_be_loaded module ')



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


def log_message():
    logger.add('./logs/logfile',
               level='INFO',
               retention='10 days',
               rotation='10 days')
    logger.info('Welcome to Python. This Module will help to load the data into postgres from mysql and files')
    return logger


def sql_alchemy_connection(env):
    try:
        config_details = read_config(env, 'POSTGRES')
        engine_string = 'postgresql://{user}:{password}@{host}:{port}/{database}'.format(**config_details)
        engine = create_engine(engine_string, echo=False)
        connection = engine.connect()
        logger.info('Connection to POSTGRES is successful through SQLALCHEMY')
        return connection
    except Exception as e:
        logger.exception('Issue in Postgres Connection Module')



def dynamically_create_insert_statement(column_names, table):
    pass



if __name__ == '__main__':
    print(log_message())
    # print(read_config('QA', 'POSTGRES'))
    # print(tables_to_be_loaded())
    # print(mysql_connection('dev'))
    print(sql_alchemy_connection('dev'))
    # print(postgres_connection('dev'))
