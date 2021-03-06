import logging
from pathlib import Path
from typing import Iterable

import jupytext
from nbformat import NotebookNode

logger = logging.getLogger(__name__)


def transform_py_to_ipynb(files: Iterable[Path]):
    for file in files:
        with file.open('r') as f_in:
            ntbk = jupytext.read(f_in)

        if is_jupytext_notebook(ntbk):
            logger.info(f'Processing {file}')
            with file.with_suffix('.ipynb').open('w') as f_out:
                jupytext.write(ntbk, f_out, fmt='ipynb')
        else:
            logger.info(f'Skipping {file} because it isn\'t a Jupytext file')


def is_jupytext_notebook(ntbk: NotebookNode) -> bool:
    # see https://github.com/mwouts/jupytext/issues/320#issuecomment-526810933
    jupytext_meta = ntbk.get('metadata', {}).get('jupytext')
    if jupytext_meta is None:
        return False
    else:
        return jupytext_meta.get('notebook_metadata_filter', '') != "-all"
