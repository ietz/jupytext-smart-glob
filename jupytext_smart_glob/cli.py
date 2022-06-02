import argparse
import logging
from pathlib import Path

from jupytext_smart_glob.transform import transform_py_to_ipynb


def main():
    logging.basicConfig()

    parser = argparse.ArgumentParser()
    parser.add_argument('directory', nargs='?', type=Path, default=Path.cwd())

    args = parser.parse_args()
    transform_py_to_ipynb(files=args.directory)
