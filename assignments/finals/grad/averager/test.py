#!/usr/bin/env python3
"""tests for averager.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './averager.py'


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert (rv > 0) if flag == '' else (rv == 0)
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def random_string():
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))


# --------------------------------------------------
def test_bad_input():
    bad = random_string()
    rv, out = getstatusoutput('{} {}'.format(prg, bad))
    assert rv == 0
    assert '"{}" is not a file'.format(bad) == out


# --------------------------------------------------
def test_no_numbers():
    file = 'inputs/no_numbers.txt'
    expected = '      0.00: no_numbers.txt'
    rv, out = getstatusoutput('{} {}'.format(prg, file))
    assert rv == 0
    assert expected == out


# --------------------------------------------------
def test_const():
    file = 'inputs/const.txt'
    expected = '      6.46: const.txt'
    rv, out = getstatusoutput('{} {}'.format(prg, file))
    assert rv == 0
    assert expected == out


# --------------------------------------------------
def test_zero():
    file = 'inputs/zero.txt'
    expected = '      0.00: zero.txt'
    rv, out = getstatusoutput('{} {}'.format(prg, file))
    assert rv == 0
    assert expected == out


# --------------------------------------------------
def test_all():
    file = 'inputs/*.txt'
    expected = """      6.46: const.txt
     -2.43: negative.txt
      0.00: no_numbers.txt
    890.00: usdeclar.txt
      0.00: zero.txt
    """.rstrip()

    rv, out = getstatusoutput('{} {}'.format(prg, file))
    assert rv == 0
    assert expected == out


# --------------------------------------------------
def test_all_and_bad():
    file = 'inputs/*.txt'
    bad = random_string()
    expected = """      6.46: const.txt
     -2.43: negative.txt
      0.00: no_numbers.txt
    890.00: usdeclar.txt
      0.00: zero.txt
    """.rstrip()

    tmp = random_string()
    try:
        rv, out = getstatusoutput('{} {} {} 2>{}'.format(prg, bad, file, tmp))
        assert os.path.isfile(tmp)

        assert open(tmp).read().rstrip() == '"{}" is not a file'.format(bad)
        assert rv == 0
        assert expected == out

    finally:
        if os.path.isfile(tmp):
            os.remove(tmp)
