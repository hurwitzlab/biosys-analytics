# Common Patters in Python

## Test argument is file and read

This program takes an argument, tests that it is a file, and then reads it. It's basically `cat`.

````
$ cat -n read_file.py
     1	#!/usr/bin/env python3
     2	"""Read a file argument"""
     3
     4	import os
     5	import sys
     6
     7	args = sys.argv[1:]
     8
     9	if len(args) != 1:
    10	    print('Usage: {} ARG'.format(os.path.basename(sys.argv[0])))
    11	    sys.exit(1)
    12
    13	filename = args[0]
    14
    15	if not os.path.isfile(filename):
    16	    print('"{}" is not a file'.format(filename), file=sys.stderr)
    17	    sys.exit(1)
    18
    19	for line in open(filename):
    20	    print(line, end='')
````
