from utils import *
import argparse



@time
def run(environment):
    modern_printer(environment)


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

    print(run(env))