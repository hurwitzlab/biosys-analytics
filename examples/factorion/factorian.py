#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-01-09
Purpose: Determine if the argument is a factorion
"""

import os
import sys


# --------------------------------------------------
def fact(n):
    if n == 0:
        return 0
    else:
        res = 1
        for i in range(1, n + 1):
            res *= i

        return res


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} NUM'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    arg = args[0]

    if arg.isdigit():
        is_factorion = False
        if int(arg) > 0:
            sum_ = 0
            for n in list(arg):
                sum_ += fact(int(n))

            if str(sum_) == arg:
                is_factorion = True

        print('"{}" is {}a factorion'.format(arg,
                                             '' if is_factorion else 'NOT '))
    else:
        print('"{}" is not a number'.format(arg))


# --------------------------------------------------
main()
