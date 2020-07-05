from utils import log_message, tables_to_be_loaded, time, read_files_to_loaded, get_current_path
from read import read_table, read_csv_file, read_excel_file
from write import write_to_table_from_table, write_to_table_from_file
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

    current_path = get_current_path()

    logger.info('=' * 50)
    logger.info('Processing of CSV starts')
    csv_details = read_files_to_loaded('CSV')
    csv_data = read_csv_file(current_path+'\\src_data\\'+csv_details['FILENAME'],csv_details['DELIMITER'])
    write_to_table_from_file(csv_details['FILENAME'].split('.')[0], csv_data, environment)
    logger.info(f'Processing of CSV ends and data is loaded into table "{csv_details["FILENAME"].split(".")[0]}"')
    logger.info('=' * 50)

    logger.info('=' * 50)
    logger.info('Processing of Excel starts')
    excel_details = read_files_to_loaded('EXCEL')
    excel_data = read_excel_file(current_path+'\\src_data\\'+excel_details['FILENAME'],excel_details['SHEET_NAME'])
    write_to_table_from_file(excel_details['FILENAME'].split('.')[0], excel_data, environment)
    logger.info(f'Processing of Excel ends and data is loaded into table "{excel_details["FILENAME"].split(".")[0]}"')
    logger.info('=' * 50)



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
        help='This is mandatory argument to denote which environment to run'
    )

    args = parser.parse_args()
    env = args.env

    run(env)