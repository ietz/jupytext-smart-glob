import argparse
import logging
from pathlib import Path
from typing import Iterable

import jupytext
from nbformat import NotebookNode

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig()

    parser = argparse.ArgumentParser()
    parser.add_argument('directory', nargs='?', type=Path, default=Path.cwd())

    args = parser.parse_args()
    transform_py_to_ipynb(files=args.directory)


def transform_py_to_ipynb(files: Iterable[Path]):
    for file in files:
        with file.open('r') as f_in:
            ntbk = jupytext.read(f_in)

        if is_jupytext_notebook(ntbk):
            with file.with_suffix('.ipynb').open('w') as f_out:
                jupytext.write(ntbk, f_out, fmt='ipynb')


def is_jupytext_notebook(ntbk: NotebookNode) -> bool:
    # see https://github.com/mwouts/jupytext/issues/320#issuecomment-526810933
    jupytext_meta = ntbk.get('metadata', {}).get('jupytext')
    if jupytext_meta is None:
        return False
    else:
        return jupytext_meta.get('notebook_metadata_filter', '') != "-all"
