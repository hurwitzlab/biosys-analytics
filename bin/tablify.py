#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@email.arizona.edu>
Date   : 2019-04-30
Purpose: Create tables
"""

import argparse
import sys
from tabulate import tabulate


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Create tables',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'file',
        metavar='FILE',
        help='Input file(s) or "-" for STDIN',
        nargs='+')

    parser.add_argument(
        '-s',
        '--sep',
        help='Field separator',
        metavar='str',
        type=str,
        default='')

    # parser.add_argument(
    #     '-i',
    #     '--int',
    #     help='A named integer argument',
    #     metavar='int',
    #     type=int,
    #     default=0)

    # parser.add_argument(
    #     '-f', '--flag', help='A boolean flag', action='store_true')

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

    for file in args.file:
        fh = None
        if file == '-':
            fh = sys.stdin
        elif os.path.isfile(file):
            fh = open(file, 'rt')

        if not fh:
            warn('Cannot open "{}"'.format(file))
            continue

        if os.path.
        _, ext = os.path.splitext
        sep = args.sep if args.sep else ',' if 

        print(tabulate(fh.read()))


# --------------------------------------------------
if __name__ == '__main__':
    main()
