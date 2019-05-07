#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-04-22
Purpose: Average all the numbers in a document
"""

import argparse
import os
import re
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Average all the numbers in a document',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'file', metavar='FILE', help='Input file(s)', nargs='+')

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

    num_re = re.compile('-?\d+(?:\.\d+)?')
    for file in args.file:
        if not os.path.isfile(file):
            warn('"{}" is not a file'.format(file))
            continue

        nums = num_re.findall(open(file).read())
        avg = 0

        if nums:
            nums = list(map(float, nums))
            avg = sum(nums)/len(nums)

        print('{:10.02f}: {}'.format(avg, os.path.basename(file)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
