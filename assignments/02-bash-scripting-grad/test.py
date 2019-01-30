#!/usr/bin/env python3
"""tests for hello.sh"""

from subprocess import getstatusoutput, getoutput
import os.path
import re

hello = "./hello.sh"
gap = "./gap.sh"


# --------------------------------------------------
def test_exists():
    """scripts exist"""
    for script in [hello, gap]:
        assert os.path.exists(script)


# --------------------------------------------------
def test_usage():
    """usage"""
    for script in [hello]:
        (retval, out) = getstatusoutput(script)
        assert retval > 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_hello_too_many():
    (retval, out) = getstatusoutput('{} {} {} {}'.format(
        hello, 'foo', 'bar', 'baz'))
    assert retval > 0
    assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_hello():
    (retval1, out1) = getstatusoutput('{} {}'.format(hello, 'Hello'))
    assert retval1 == 0
    assert out1 == 'Hello, Human!'

    (retval2, out2) = getstatusoutput('{} "{}" "{}"'.format(
        hello, 'Good Day', 'Kind Sir'))
    assert retval2 == 0
    assert out2 == 'Good Day, Kind Sir!'


# --------------------------------------------------
def test_gap():
    (retval1, out1) = getstatusoutput(gap)
    assert retval1 == 0
    assert len(out1.split('\n')) >= 142

    (retval2, out2) = getstatusoutput('{} {}'.format(gap, 'b'))
    assert retval2 == 0
    assert len(out2.split('\n')) == 11

    (retval3, out3) = getstatusoutput('{} {}'.format(gap, 'q'))
    assert retval3 == 0
    assert out3 == 'There are no countries starting with "q"'

    (retval4, out4) = getstatusoutput('{} "{}"'.format(gap, '[u-z]'))
    assert retval4 == 0
    assert len(out4.split('\n')) == 10
