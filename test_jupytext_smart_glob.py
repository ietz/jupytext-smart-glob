import jupytext
import pytest
from nbformat.v4 import new_notebook, new_code_cell

from jupytext_smart_glob import is_jupytext_notebook

plain_py_content = "print('Hello world!')\n"
jupytext_py_percent_content = jupytext.writes(
    fmt='py:percent',
    notebook=new_notebook(
        cells=[
            new_code_cell(plain_py_content),
        ],
    ),
)


@pytest.mark.parametrize(
    ('content', 'has_metadata'),
    [
        (plain_py_content, False),
        (jupytext_py_percent_content, True),
    ]
)
def test_is_jupytext_notebook(content: str, has_metadata: bool):
    assert is_jupytext_notebook(jupytext.reads(content)) == has_metadata
