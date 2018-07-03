import os.path

import pytest

from mod import f

@pytest.fixture
def no_txt_dir(tmpdir):
    with open(str(tmpdir.join('no.txt')), 'x'):
        pass
    return tmpdir

def test_f(tmpdir):
    exp = 42
    f(tmpdir)
    with open(str(tmpdir.join('yes.txt')), 'r') as fhandle:
        obs = int(fhandle.read())
    assert obs == exp

def test_f_with_no(no_txt_dir):
    f(no_txt_dir)
    assert not os.path.exists(str(no_txt_dir.join('yes.txt')))