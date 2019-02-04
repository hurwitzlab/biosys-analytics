#!/usr/bin/env python3
"""tests for cat-n.py, head.py"""

from subprocess import getstatusoutput, getoutput
import os.path
import re

cat_n = "./cat_n.py"
head = "./head.py"
sonnet = 'files/sonnet-29.txt'
issa = 'files/issa.txt'


def test_usage_catn():
    """usage catn"""
    (retval, out) = getstatusoutput(cat_n)
    assert retval > 0
    assert re.match("usage", out, re.IGNORECASE)


def test_usage_head():
    """usage head"""
    (retval, out) = getstatusoutput(head)
    assert retval > 0
    assert re.match("usage", out, re.IGNORECASE)


def test_bad_input_catn():
    """bad input catn"""
    (retval, out) = getstatusoutput('{} {}'.format(cat_n, 'foo'))
    assert retval > 0
    assert out == 'foo is not a file'


def test_bad_number_head():
    """bad number catn"""
    (rv1, out1) = getstatusoutput('{} {} {}'.format(head, sonnet, '-1'))
    assert rv1 > 0
    assert out1 == 'lines (-1) must be a postive number'

    (rv2, out2) = getstatusoutput('{} {} {}'.format(head, issa, '0'))
    assert out2 == 'lines (0) must be a postive number'


def test_bad_input_head():
    """bad input catn"""
    (retval, out) = getstatusoutput('{} {}'.format(head, 'foo'))
    assert retval > 0
    assert out == 'foo is not a file'


def test_catn_run():
    """runs ok"""
    cat_re = re.compile(r'^\s+\d+:.*$')

    for file in [sonnet, issa]:
        assert os.path.exists(file)

        (rv, out) = getstatusoutput("{} {}".format(cat_n, file))

        assert rv == 0

        num_lines = len(open(file).readlines())
        out_lines = out.split('\n')
        assert len(out_lines) == num_lines

        assert all(map(lambda s: cat_re.match(s), out_lines))


def test_head_run():
    """runs ok"""
    for file in [sonnet, issa]:
        for num in [1, 3, 5, 9]:
            out = getoutput("{} {} {}".format(head, file, num))
            out_lines = out.split('\n')
            assert len(out_lines) == num
