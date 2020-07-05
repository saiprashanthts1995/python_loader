from utils import dynamically_create_insert_statement, log_message, postgres_connection, sql_alchemy_connection, truncate_query
from read import read_table


def truncate_table(environment, table_name):
    logger = log_message()
    try:
        connection = postgres_connection(environment)
        cursor = connection.cursor()
        truncate_statement = truncate_query(table_name)
        cursor.execute(truncate_statement)
        logger.info('Truncated the data present in {} table'.format(table_name))
    except:
        logger.exception('Issue occurred for truncating the data into {} table'.format(table_name))
    finally:
        connection.commit()
        connection.close()


def write_to_table_from_table(data_to_be_loaded, column_names_of_table, env, table_name):
    logger = log_message()
    try:
        connection = postgres_connection(env)
        truncate_table(env, table_name)
        cursor = connection.cursor()
        insert_query = dynamically_create_insert_statement(column_names_of_table, table_name)
        cursor.executemany(insert_query, data_to_be_loaded)
        logger.info('Successfully written the data into {} table'.format(table_name))
    except:
        logger.exception('Issue occurred for loading the data into {} table'.format(table_name))
    finally:
        connection.commit()
        connection.close()


def write_to_table_from_file(table_name, data_to_be_loaded, env):
    logger = log_message()
    try:
        connection = sql_alchemy_connection(env)
        data_to_be_loaded.to_sql(name=table_name, if_exists='replace', index=False, con=connection)
        logger.info('Successfully written the data into {} table using sqlalchemy'.format(table_name))
    except:
        logger.exception('Issue occurred for loading the data into {} table using sqlalchemy'.format(table_name))
    finally:
        connection.close()


if __name__ == '__main__':
    data, column_names = read_table('dev', 'departments')
    write_to_table_from_table(data, column_names, 'dev', 'departments')