#!/usr/bin/env python3
"""tests for upgoer.py"""

import os
import random
import re
import string
from subprocess import getoutput, getstatusoutput

prg = "./upgoer.py"
hello = 'hello.txt'
nobody = 'nobody.txt'
gettysburg = 'gettysburg.txt'


# --------------------------------------------------
def random_string():
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))


# --------------------------------------------------
def test_usage():
    """usage"""
    for help_flag in ['', '-h', '--help']:
        out = getoutput('{} {}'.format(prg, help_flag))
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_wordlist():
    """bad wordlist"""
    for flag in ['-w', '--wordlist']:
        bad = random_string()
        rv, out = getstatusoutput('{} {} {} {}'.format(prg, flag, bad, hello))
        assert rv > 0
        assert out == '"{}" is not a file'.format(bad)


# --------------------------------------------------
def test_bad_input():
    """bad_input"""
    bad = random_string()
    rv, out = getstatusoutput('{} {}'.format(prg, bad))
    assert rv > 0
    assert out == '"{}" is not a file'.format(bad)


# --------------------------------------------------
def test_hello():
    rv1, out1 = getstatusoutput('{} {}'.format(prg, hello))
    assert rv1 == 0
    expected1 = '  1: hello\n1 word to change.'
    assert expected1 == out1

    tmp = random_string()
    rv2, out2 = getstatusoutput('{} {} 2>{}'.format(prg, hello, tmp))

    try:
        assert os.path.isfile(tmp)
        expected2 = '1 word to change.'
        assert expected2 == out2

        stderr = open(tmp).read().rstrip()
        assert stderr == '  1: hello'

    finally:
        if os.path.isfile(tmp):
            os.remove(tmp)


# --------------------------------------------------
def test_nobody():
    rv1, out1 = getstatusoutput('{} {}'.format(prg, nobody))
    assert rv1 == 0
    expected1 = """  1: i'm
  2: nobody
  3: nobody
  4: theres
  5: dont
  6: theyd
  7: advertise
  8: dreary
  9: somebody
 10: public
 11: frog
 12: one's
 13: livelong
 14: june
 15: admiring
 16: bog
16 words to change.
""".rstrip()
    assert expected1 == out1

    tmp = random_string()
    rv2, out2 = getstatusoutput('{} {} 2>{}'.format(prg, nobody, tmp))

    try:
        assert os.path.isfile(tmp)
        expected2 = '16 words to change.'
        assert expected2 == out2

        stderr = open(tmp).read().rstrip()
        assert stderr == '\n'.join(expected1.split('\n')[:-1])

    finally:
        if os.path.isfile(tmp):
            os.remove(tmp)


# --------------------------------------------------
def test_gettysburg():
    rv1, out1 = getstatusoutput('{} {}'.format(prg, gettysburg))
    assert rv1 == 0
    expected1 = """  1: years
  2: fathers
  3: forth
  4: conceived
  5: liberty
  6: dedicated
  7: proposition
  8: created
  9: engaged
 10: civil
 11: testing
 12: conceived
 13: dedicated
 14: endure
 15: met
 16: battlefield
 17: dedicate
 18: portion
 19: resting
 20: lives
 21: altogether
 22: fitting
 23: larger
 24: not
 25: dedicate
 26: not
 27: consecrate
 28: not
 29: hallow
 30: brave
 31: living
 32: struggled
 33: consecrated
 34: detract
 35: forget
 36: living
 37: dedicated
 38: unfinished
 39: fought
 40: nobly
 41: advanced
 42: dedicated
 43: task
 44: remaining
 45: honored
 46: increased
 47: devotion
 48: devotion
 49: highly
 50: resolve
 51: not
 52: died
 53: vain
 54: god
 55: birth
 56: freedom
 57: government
 58: not
 59: perish
59 words to change.
""".rstrip()
    assert expected1 == out1

    tmp = random_string()
    rv2, out2 = getstatusoutput('{} {} 2>{}'.format(prg, gettysburg, tmp))

    try:
        assert os.path.isfile(tmp)
        expected2 = '59 words to change.'
        assert expected2 == out2

        stderr = open(tmp).read().rstrip()
        assert stderr == '\n'.join(expected1.split('\n')[:-1])

    finally:
        if os.path.isfile(tmp):
            os.remove(tmp)
