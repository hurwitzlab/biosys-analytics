#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-04-23
Purpose: Pig Latin
"""

import argparse
import os
import re
import string
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Convert to Pig Latin',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'input', metavar='STR', help='Input text or file')

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    input_ = args.input
    text = open(input_).read() if os.path.isfile(input_) else input_

    for line in text.split('\n'):
        for word in line.split():
            clean = re.sub("[^a-zA-Z0-9']", '', word)
            print(pig(clean), end=' ')

        print()


# --------------------------------------------------
def pig(word):
    """Create Pig Latin version of a word"""

    consonants = re.sub('[aeiouAEIOU]', '', string.ascii_letters)
    match = re.match('^([' + consonants + ']+)(.+)', word)
    if match:
        return '-'.join([match.group(2), match.group(1) + 'ay'])
    else:
        return word + '-yay'


# --------------------------------------------------
if __name__ == '__main__':
    main()
