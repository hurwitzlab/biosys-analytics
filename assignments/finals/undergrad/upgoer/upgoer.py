#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@email.arizona.edu>
Date   : 2019-04-22
Purpose: Find words in text not in 1000 most-common
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
        description='Find words in text not in 1000 most-common',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file', metavar='FILE', help='File to check')

    parser.add_argument(
        '-w',
        '--wordlist',
        help='Common word file',
        metavar='str',
        type=str,
        default='1000.txt')

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
    file = args.file
    wordlist = args.wordlist

    for fname in [file, wordlist]:
        if not os.path.isfile(fname):
            die('"{}" is not a file'.format(fname))

    common = set()
    for line in open(wordlist):
        for word in line.rstrip().split():
            common.add(word)

    num_bad = 0
    for line in open(file):
        for word in line.lower().split():
            clean = re.sub("[^a-zA-Z0-9']", '', word)
            if clean and clean not in common:
                num_bad += 1
                warn('{:3}: {}'.format(num_bad, clean))

    print('{} word{} to change.'.format(num_bad, '' if num_bad == 1 else 's'))


# --------------------------------------------------
if __name__ == '__main__':
    main()
