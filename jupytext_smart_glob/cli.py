import argparse
import glob
import logging
from pathlib import Path
from typing import List, Iterable

from jupytext_smart_glob.transform import transform_py_to_ipynb


def main():
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='*')

    args = parser.parse_args()
    transform_py_to_ipynb(
        files=get_files_matching_patterns(args.files) if len(args.files) > 0 else Path.cwd().rglob('**/*.py')
    )


def get_files_matching_patterns(patterns: List[str]) -> Iterable[Path]:
    for pattern in patterns:
        if "*" in pattern or "?" in pattern:
            for file_str in glob.glob(pattern, recursive=True):
                yield Path(file_str)
        else:
            file = Path(pattern)
            if file.is_file():
                yield file
