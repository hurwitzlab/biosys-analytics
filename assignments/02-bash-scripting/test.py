#!/usr/bin/env python3
"""tests for cat-n.sh, head.sh"""

from subprocess import getstatusoutput, getoutput
import os.path
import re

cat_n = "./cat-n.sh"
head = "./head.sh"


def head_file(file, n=3):
    lines = []
    for i, line in enumerate(open(file)):
        lines.append(line)
        if i + 1 == n:
            break
    return ''.join(lines)


def test_exists():
    """scripts exist"""
    for script in [cat_n, head]:
        assert os.path.exists(script)


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


def test_bad_input_head():
    """bad input catn"""
    (retval, out) = getstatusoutput('{} {}'.format(head, 'foo'))
    assert retval > 0
    assert out == 'foo is not a file'


def test_catn_run():
    """runs ok"""
    for file in ["files/sonnet-29.txt", "files/issa.txt"]:
        assert os.path.exists(file)

        fh = open(file, "r")
        expected = "".join(
            map(lambda x: '{} {}'.format(x[0] + 1, x[1]),
                enumerate(fh.readlines())))

        (retval, output) = getstatusoutput("{} {}".format(cat_n, file))

        assert retval == 0
        assert output.rstrip() == expected.rstrip()


def test_head_run():
    """runs ok"""
    for (file, num) in [("files/sonnet-29.txt", 3), ("files/issa.txt", 10)]:
        out = getoutput("{} {} {}".format(head, file, num))
        expected = head_file(file, num)
        assert out.rstrip() == expected.rstrip()
