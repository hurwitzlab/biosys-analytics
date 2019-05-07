#!/usr/bin/env python3

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './piggie.py'


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert (rv > 0) if flag == '' else (rv == 0)
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def run_text(in_text, expected):
    """Run with text input"""

    rv, out = getstatusoutput('{} "{}"'.format(prg, in_text))
    assert rv == 0
    assert expected.rstrip() == out.rstrip()


# --------------------------------------------------
def test_text1():
    """text input"""

    run_text('foo arf chaz', 'oo-fay arf-yay az-chay')


# --------------------------------------------------
def test_text2():
    """text input"""

    run_text('Somewhere, over the rainbow',
             'omewhere-Say over-yay e-thay ainbow-ray')


# --------------------------------------------------
def run_file(file):
    """Run with file input"""

    rv, out = getstatusoutput('{} "{}"'.format(prg, file))

    assert rv == 0

    basename = os.path.basename(file)
    expected_file = os.path.join('test-outs', basename)
    expected = open(expected_file).read()
    assert expected == out


# --------------------------------------------------
def test_nobody():
    """Emily Dickinson input"""

    run_file('inputs/nobody.txt')


# --------------------------------------------------
def test_usdeclar():
    """US Declaration input"""

    run_file('inputs/usdeclar.txt')


# --------------------------------------------------
def test_gettysburg():
    """gettysburg input"""

    run_file('inputs/gettysburg.txt')
