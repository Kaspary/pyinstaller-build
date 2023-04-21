import argparse
import logging
import os
from logging.config import dictConfig as logging_dict_config
import traceback

from PyInstaller.__main__ import run as run_pyinstaller

ROOT_DIR = os.getcwd()
BUILD_DIR = os.path.join(ROOT_DIR, 'src', 'build')
DIST_DIR = os.path.join(BUILD_DIR, 'dist')

os.makedirs(BUILD_DIR, exist_ok=True)
logging_dict_config({
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s] [%(levelname)s]: %(message)s'
        }
    },
    'handlers': {
        'streamHandler': {
            'level': 'NOTSET',
            'formatter': 'standard',
            'class': 'logging.StreamHandler'
        },
        'fileHandler': {
            'level': 'NOTSET',
            'formatter': 'standard',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': f"{BUILD_DIR}/build.log",
            'mode': 'w',
            'backupCount': 0
        }
    },
    'loggers': {
        '': {
            'handlers': ['streamHandler', 'fileHandler'],
            'propagate': False
        }
    }
})

parser = argparse.ArgumentParser(description='Build python scripts.')

class ValidatePythonScript(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if not values.endswith('.py'):
            parser.error(f"Invalid python script, got: {values}")
        if not os.path.isfile(values):
            parser.error(f"Script {repr(values)} not found")
        setattr(namespace, self.dest, values)


parser.add_argument(
    'setup_script',
    type=str,
    action=ValidatePythonScript,
    help='script path to build')

parser.add_argument(
    '--no-cache',
    default=False,
    action='store_true',
    dest='no_cache',
    help='clean pyinstaller cache and remove temporary files'
)

args = parser.parse_args()

def setup():
    pyinstaller_args = [
        args.setup_script,
        '--onefile',
        '--distpath', DIST_DIR,
        '--workpath', BUILD_DIR,
        '--specpath', BUILD_DIR
    ]

    if args.no_cache:
        logging.info('Clean build cache')
        pyinstaller_args.append('--clean')

    logging.info(f"Build script {repr(args.setup_script)}")
    build(pyinstaller_args)
    logging.info(f"Build completed, accessible in {repr(DIST_DIR)}")


def build(params):
    run_pyinstaller(params)


if __name__ == '__main__':
    try:
        setup()
    except Exception as e:
        logging.error(f"{str(e)}: {traceback.format_exc()}")
    finally:
        logging.info('Done!')
