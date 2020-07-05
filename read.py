from utils import mysql_connection, log_message
import pandas as pd


# read csv files
def read_table(env, table):
    logger = log_message()
    try:
        connection = mysql_connection(env)
        cursor = connection.cursor()
        cursor.execute('select * from {}'.format(table))
        logger.info('Successfully read the {} table'.format(table))
        return cursor.fetchall()
    except:
        logger.exception('Issue occurred while reading the content of {} table'.format(table))


def read_csv_file(file_name, sep_of_file):
    logger = log_message()
    try:
        csv_data = pd.read_csv(file_name, sep = sep_of_file)
        logger.info('Successfully read the CSV file named {}'.format(file_name))
        return csv_data
    except:
        logger.exception('Issue occurred while reading the content of {} table'.format(file_name))


def read_excel_file(file_name, sheet_name):
    logger = log_message()
    try:
        excel_data = pd.read_excel(file_name, sheet_name= sheet_name)
        logger.info('Successfully read the Excel file named {}'.format(file_name))
        return excel_data
    except:
        logger.exception('Issue occurred while reading the content of {} table'.format(file_name))


if __name__ == '__main__':
    print(read_table('dev', 'departments'))
