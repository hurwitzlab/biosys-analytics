#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-02-22
Purpose: Rock the Casbah
"""

import os
import re
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    file = args[0]

    float_ = r'[+-]?\d+\.*\d*'
    line_re = re.compile('^attr\.([^\s]+)\s+:\s+(.+)$')
    ll1 = re.compile('(' + float_ + ')\s*[,_]\s*(' + float_ + ')')
    ll2 = re.compile('(' + float_ + ')(?:\s*([NS]))?(?:\s*,)?\s+(' + float_ +
                     ')(?:\s*([EW])?)')

    loc_hms = r"""
    \d+\.\d+'\d+\.\d+"
    """.strip()
    ll3 = re.compile('(' + loc_hms + ')\s+(' + loc_hms + ')')

    for line in open(file):
        match = line_re.search(line)
        if match:
            fld, val = match.group(1), match.group(2)
            print('{} = {}'.format(fld, val))

            if fld == 'lat_lon':
                ll_match1 = ll1.search(val)
                ll_match2 = ll2.search(val)
                ll_match3 = ll3.search(val)

                if ll_match1:
                    lat, lon = ll_match1.group(1), ll_match1.group(2)
                    lat = float(lat)
                    lon = float(lon)
                    print('lat = {}, lon = {}'.format(lat, lon))
                elif ll_match2:
                    lat, lat_dir, lon, lon_dir = ll_match2.group(
                        1), ll_match2.group(2), ll_match2.group(
                            3), ll_match2.group(4)
                    lat = float(lat)
                    lon = float(lon)

                    if lat_dir == 'S':
                        lat *= -1

                    if lon_dir == 'W':
                        lon *= -1
                    print('lat = {}, lon = {}'.format(lat, lon))
                elif ll_match3:
                    lat, lon = ll_match3.group(1), ll_match3.group(2)
                    print('lat = {}, lon = {}'.format(lat, lon))
                else:
                    print('No match')


# --------------------------------------------------
main()
