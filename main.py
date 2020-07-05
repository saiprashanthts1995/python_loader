from utils import log_message, tables_to_be_loaded, time
from read import read_table
from write import write_to_table_from_table
from test import count_check
import argparse



@time
def run(environment):
    logger = log_message()
    logger.info('Welcome to Python. This Module will help to load the data into postgres from mysql and files')
    logger.info('Started loading the data into the environment {}'.format(environment))

    tables_to_loaded = tables_to_be_loaded()

    for each_table in tables_to_loaded:
        logger.info('='*50)
        logger.info('Process for the table {} started'.format(each_table))
        logger.info('-'*50)

        logger.info('Reading for the table {} started'.format(each_table))
        data, column_names = read_table(environment, each_table)
        logger.info('Reading for the table {} completed'.format(each_table))

        logger.info('writing for the table {} started'.format(each_table))
        write_to_table_from_table(data, column_names, environment, each_table)
        logger.info('writing for the table {} completed'.format(each_table))

        logger.info('checking for the table {} started'.format(each_table))
        count_check(environment, each_table)
        logger.info('checking for the table {} completed'.format(each_table))
        logger.info('=' * 50)

    logger.info('Overall Process Completed')


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description= 'To load arguments required for the process',
        prog='main.py'
    )

    parser.add_argument(
        '--env',
        '-e',
        dest='env',
        required=True,
        choices=['DEV', 'QA'],
        help= 'This is mandatory argument to denote which environment to run'
    )

    args = parser.parse_args()
    env = args.env

    run(env)