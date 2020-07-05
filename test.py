from utils import mysql_connection, postgres_connection, read_queries_from_yaml, log_message


def count_check(environment, table_name):
    logger = log_message()
    queries = read_queries_from_yaml()
    check_query = (queries['queries']['count_query']).format(table_name)
    try:
        mysql_conn = mysql_connection(environment)
        psql_conn = postgres_connection(environment)
        cursor_mysql = mysql_conn.cursor()
        cursor_psql = psql_conn.cursor()
        cursor_mysql.execute(check_query)
        src_count = cursor_mysql.fetchone()[0]
        cursor_psql.execute(check_query)
        tgt_count = cursor_psql.fetchone()[0]
        logger.info('Table Count  for the {} table in Source Database is {}'.format(table_name, src_count))
        logger.info('Table Count  for the {} table in Source Database is {}'.format(table_name, tgt_count))
        if tgt_count == src_count:
            logger.info('Count check  for the {} table passed successfully'.format(table_name))
        else:
            logger.error('Count check  for the {} table failed'.format(table_name))
    except:
        logger.exception('Issue occurred for truncating the data into {} table'.format(table_name))
    finally:
        mysql_conn.close()
        psql_conn.close()


if __name__ == '__main__':
    print(count_check('dev', 'departments'))