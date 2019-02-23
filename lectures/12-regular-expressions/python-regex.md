# Regular Expressions

The term "regular expression" is a formal, linguistic term that describes the ability to desc you might be interested to read about (https://en.wikipedia.org/wiki/Regular_language). For our purposes, regular expressions (AKA "regexes" or a "regex") is a way to formally describe some string that we want to find. Regexes are a DSL (domain-specific language) that we use inside Python, just like in the previous chapter we use SQL statements to communite with SQLite. We can `import re` to use the Python regular expression module and use it to search text.

# ENA Metadata

Let's examine the ENA metadata from the XML parsing example:

````
$ ./xml_ena.py *.xml | grep lat_lon
attr.lat_lon             : 27.83387,-65.4906
attr.lat_lon             : 29.3 N 122.08 E
attr.lat_lon             : 28.56_-88.70377
attr.lat_lon             : 39.283N 76.611 W
attr.lat_lon             : 78 N 5 E
attr.lat_lon             : missing
attr.lat_lon             : 0.00 N, 170.00 W
attr.lat_lon             : 11.46'45.7" 93.01'22.3"
````

We see there are many ways that latitude/longitude have been represented. Look at "collection_date":

````
$ ./xml_ena.py *.xml | grep collection
attr.collection_date     : March 24, 2014
attr.collection_date     : 2013-08-15/2013-08-28
attr.collection_date     : 20100910
attr.collection_date     : 02-May-2012
attr.collection_date     : Jul-2009
attr.collection_date     : missing
attr.collection_date     : 2013-12-23
attr.collection_date     : 5/04/2012
````

How can we go about parsing all the various ways this data has been encoded? Regular expressions provide us a way to describe in very specific way what we want. 

Let's start just with the idea of matching a number (where "number" is a string that could be parsed into a number) like "27.83387":

````
>>> import re
>>> n1 = '27.83387'
>>> re.search('\d', n1)
<_sre.SRE_Match object; span=(0, 1), match='2'>
````

The `\d` pattern means "any number" which is the same as `[0-9]` where the `[]` creates a class of characters and `0-9` expands to all the numbers from zero to nine. The problem is that it only matches one number, `2`. Change it to `\d+` to indicate "one or more numbers":

````
>>> re.search('\d+', n1)
<_sre.SRE_Match object; span=(0, 2), match='27'>
````

Now let's capture the decimal point: 

````
>>> re.search('\d+.', n1)
<_sre.SRE_Match object; span=(0, 3), match='27.'>
````

You migth think that's perfect, but the `.` has a special meaning in regex. It means "one of anything", so it matches this, too:

````
>>> re.search('\d+.', '27x83387')
<_sre.SRE_Match object; span=(0, 3), match='27x'>
````

To indicate we want a literal `.` we have to make it `\.` (backslash-escape):

````
>>> re.search('\d+\.', n1)
<_sre.SRE_Match object; span=(0, 3), match='27.'>
>>> re.search('\d+\.', '27x83387')
````

Notice that the second try returns nothing.

To capture the bit after the `.`, add more numbers:

````
>>> re.search('\d+\.\d+', n1)
<_sre.SRE_Match object; span=(0, 8), match='27.83387'>
````

But we won't always see floats. Can we make this regex match integers, too? We can indicate that part of a pattern is optional by putting a `?` after it. Since we need more than one thing to be optional, we need to wrap it in parens:

````
>>> re.search('\d+\.\d+', '27')
>>> re.search('\d+(\.\d+)?', '27')
<_sre.SRE_Match object; span=(0, 2), match='27'>
>>> re.search('\d+(\.\d+)?', n1)
<_sre.SRE_Match object; span=(0, 8), match='27.83387'>
````

What if there is a negative symbol in front? Add `-?` (an optional dash) at the beginning:

````
>>> re.search('-?\d+(\.\d+)?', '-27.83387')
<_sre.SRE_Match object; span=(0, 9), match='-27.83387'>
>>> re.search('-?\d+(\.\d+)?', '27.83387')
<_sre.SRE_Match object; span=(0, 8), match='27.83387'>
>>> re.search('-?\d+(\.\d+)?', '-27')
<_sre.SRE_Match object; span=(0, 3), match='-27'>
>>> re.search('-?\d+(\.\d+)?', '27')
<_sre.SRE_Match object; span=(0, 2), match='27'>
````

Sometimes we actually find a `+` at the beginning, so we can make an optional character class `[+-]?`:

````
>>> re.search('[+-]?\d+(\.\d+)?', '-27.83387')
<_sre.SRE_Match object; span=(0, 9), match='-27.83387'>
>>> re.search('[+-]?\d+(\.\d+)?', '+27.83387')
<_sre.SRE_Match object; span=(0, 9), match='+27.83387'>
>>> re.search('[+-]?\d+(\.\d+)?', '27.83387')
<_sre.SRE_Match object; span=(0, 8), match='27.83387'>
````

Now we can match things that basically look like a floating point number or an integer, both positive and negative.

There are many resources you can use to thoroughly learn regular expressions, so I won't try to cover them completely here. I will mostly try to introduce the general idea and show you some useful regexes you could steal.

Here is an example of how you can embed regexes in your Python code. This version can parse all the versions of latitude/longitude shown above:

````
$ cat -n ena_re.py
     1	#!/usr/bin/env python3
     2	"""
     3	Author : kyclark
     4	Date   : 2019-02-22
     5	Purpose: Rock the Casbah
     6	"""
     7
     8	import os
     9	import re
    10	import sys
    11
    12
    13	# --------------------------------------------------
    14	def main():
    15	    args = sys.argv[1:]
    16
    17	    if len(args) != 1:
    18	        print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
    19	        sys.exit(1)
    20
    21	    file = args[0]
    22
    23	    float_ = r'[+-]?\d+\.*\d*'
    24	    line_re = re.compile('^attr\.([^\s]+)\s+:\s+(.+)$')
    25	    ll1 = re.compile('(' + float_ + ')\s*[,_]\s*(' + float_ + ')')
    26	    ll2 = re.compile('(' + float_ + ')(?:\s*([NS]))?(?:\s*,)?\s+(' + float_ +
    27	                     ')(?:\s*([EW])?)')
    28
    29	    loc_hms = r"""
    30	    \d+\.\d+'\d+\.\d+"
    31	    """.strip()
    32	    ll3 = re.compile('(' + loc_hms + ')\s+(' + loc_hms + ')')
    33
    34	    for line in open(file):
    35	        match = line_re.search(line)
    36	        if match:
    37	            fld, val = match.group(1), match.group(2)
    38	            print('{} = {}'.format(fld, val))
    39
    40	            if fld == 'lat_lon':
    41	                ll_match1 = ll1.search(val)
    42	                ll_match2 = ll2.search(val)
    43	                ll_match3 = ll3.search(val)
    44
    45	                if ll_match1:
    46	                    lat, lon = ll_match1.group(1), ll_match1.group(2)
    47	                    lat = float(lat)
    48	                    lon = float(lon)
    49	                    print('lat = {}, lon = {}'.format(lat, lon))
    50	                elif ll_match2:
    51	                    lat, lat_dir, lon, lon_dir = ll_match2.group(
    52	                        1), ll_match2.group(2), ll_match2.group(
    53	                            3), ll_match2.group(4)
    54	                    lat = float(lat)
    55	                    lon = float(lon)
    56
    57	                    if lat_dir == 'S':
    58	                        lat *= -1
    59
    60	                    if lon_dir == 'W':
    61	                        lon *= -1
    62	                    print('lat = {}, lon = {}'.format(lat, lon))
    63	                elif ll_match3:
    64	                    lat, lon = ll_match3.group(1), ll_match3.group(2)
    65	                    print('lat = {}, lon = {}'.format(lat, lon))
    66	                else:
    67	                    print('No match')
    68
    69
    70	# --------------------------------------------------
    71	main()
$ cat re.txt
attr.lat_lon             : 27.83387,-65.4906
attr.lat_lon             : 29.3 N 122.08 E
attr.lat_lon             : 28.56_-88.70377
This line will not be included
attr.lat_lon             : 39.283N 76.611 W
attr.lat_lon             : 78 N 5 E
attr.lat_lon             : missing
attr.lat_lon             : 0.00 N, 170.00 W
attr.lat_lon             : 11.46'45.7" 93.01'22.3"
$ ./ena_re.py re.txt
lat_lon = 27.83387,-65.4906
lat = 27.83387, lon = -65.4906
lat_lon = 29.3 N 122.08 E
lat = 29.3, lon = 122.08
lat_lon = 28.56_-88.70377
lat = 28.56, lon = -88.70377
lat_lon = 39.283N 76.611 W
lat = 39.283, lon = -76.611
lat_lon = 78 N 5 E
lat = 78.0, lon = 5.0
lat_lon = missing
No match
lat_lon = 0.00 N, 170.00 W
lat = 0.0, lon = -170.0
lat_lon = 11.46'45.7" 93.01'22.3"
lat = 11.46'45.7", lon = 93.01'22.3"
````