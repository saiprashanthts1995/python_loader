from mysql import connector as mc
import datetime

def mysql_connection(env):
    pass


def postgres_connection(env):
    pass


def read_config(env):
    pass


def tables_to_be_loaded():
    pass


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
