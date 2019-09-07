#######################################
# Script to start and remove database #
#######################################

import argparse
from pathlib import Path

import shutil
import subprocess

from nflpicks.utils.logs import logging



parser = argparse.ArgumentParser()
parser.add_argument('-db',  nargs='?', type=str,
        help='start/remove database\n\te.g. python manager -db start')


args = parser.parse_args()

def start_db():
    try:
        logging.info('Initializing DataBase Mirgrate and Upgrade')
        subprocess.run(['flask', 'db', 'init'])
        subprocess.run(['flask', 'db', 'migrate', '-m', 'moving files'])
        subprocess.run(['flask', 'db', 'upgrade'])

    except Exception as e:
        logging.error('Issues starting DataBase', exc_info=True)
        return 1
    logging.info('Initializing Completed')
    return 0


def delete_db():
    try:
        logging.info('Deleting DataBase')
        input('> [Y/n] Press Enter for Y, Ctrl+C to cancel')
        shutil.rmtree('migrations')
        db = Path('nflpicks/data/data.sqlite')
        db.unlink()
    except Exception as e:
        logging.error('Issues starting DataBase', exc_info=True)
        return 1
    logging.info('DataBase Deleted')
    return 0


if args.db == 'start':
    start_db()
elif args.db == 'remove':
    delete_db()
else:
    raise ValueError('Command Unknown. Try python manager.py -h')
    pass

    
