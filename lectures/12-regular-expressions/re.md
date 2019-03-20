
# Introduction to Regular Expressions in Python

To use regular expressions:


```python
import re
```


```python
# How do we match a number?
print(re.match('1', '1'))
```

    <_sre.SRE_Match object; span=(0, 1), match='1'>



```python
# But that only works for just "1"
print(re.match('2', '1'))
```

    None



```python
# How do we match all the numbers from 0 to 9? 
re.match('[0-9]', '1')
```




    <_sre.SRE_Match object; span=(0, 1), match='1'>




```python
# There is a short-hand for the character class `[0-9]` that is `\d` (digit)
re.match('\d', '1')
```




    <_sre.SRE_Match object; span=(0, 1), match='1'>




```python
# But this only matches the first number we see
re.match('\d', '123')
```




    <_sre.SRE_Match object; span=(0, 1), match='1'>




```python
# We can use `{}` to indicate `{min,max}`, `{min,}`, `{,max}`, or `{exactly}`
print(re.match('\d{1,4}', '1234567890'))
print(re.match('\d{1,}', '1234567890'))
print(re.match('\d{,5}', '1234567890'))
print(re.match('\d{8}', '1234567890'))
```

    <_sre.SRE_Match object; span=(0, 4), match='1234'>
    <_sre.SRE_Match object; span=(0, 10), match='1234567890'>
    <_sre.SRE_Match object; span=(0, 5), match='12345'>
    <_sre.SRE_Match object; span=(0, 8), match='12345678'>



```python
# What if we wanted to recognize a US SSN (social security number)? 
# We will use `re.compile` to create the regex and use it in a `for` loop 
ssn_re = re.compile('\d{3}-\d{2}-\d{4}')
for s in ['123456789', '123-456-789', '123-45-6789']:
    print('{}: {}'.format(s, ssn_re.match(s)))
```

    123456789: None
    123-456-789: None
    123-45-6789: <_sre.SRE_Match object; span=(0, 11), match='123-45-6789'>



```python
# SSNs always use a dash (`-`) as a number separator, but dates do not
date_re = re.compile('\d{4}-\d{2}-\d{2}')
dates = ['1999-01-01', '1999/01/01']
for d in dates:
    print('{}: {}'.format(d, date_re.match(d)))
```

    1999-01-01: <_sre.SRE_Match object; span=(0, 10), match='1999-01-01'>
    1999/01/01: None



```python
# Just as we created a character class with `[0-9]` to 
# represent all the numbers from 0 to 9,
# we can create a class to represent the separators "/" and "-" 
# with `[/-]`
# As regular expressions get longer, it makes sense to break
# each unit onto a different line and use Python's literal 
# string expression to join them into a single string.
# As a bonus, we can comment on each unit of the regex.

date_re = re.compile('\d{4}'  # year
                     '[/-]'   # separator
                     '\d{2}'  # month
                     '[/-]'   # separator
                     '\d{2}') # day

dates = ['1999-01-01', '1999/01/01']
for d in dates:
    print('{}: {}'.format(d, date_re.match(d)))
```

    1999-01-01: <_sre.SRE_Match object; span=(0, 10), match='1999-01-01'>
    1999/01/01: <_sre.SRE_Match object; span=(0, 10), match='1999/01/01'>



```python
# If we wanted to extract each part of the date (year, month, day),
# we can use parentheses `()` around the parts we want to capture 
# into `groups`. The group "0" is the whole string that was match, 
# and they are numbered sequentially after that for each group
#
# Can you change the regex to match all three strings?
date_re = re.compile('(\d{4})'
                     '[/-]'
                     '(\d{2})'
                     '[/-]'
                     '(\d{2})')

dates = ['1999-01-01', '1999/01/01', '1999.01.01']
for d in dates:
    match = date_re.match(d)
    print('{}: {}'.format(d, 'match' if match else 'miss'))
    if match:
        print(match.groups())
        print('year:', match.group(1))
    print()
```

    1999-01-01: match
    ('1999', '01', '01')
    year: 1999
    
    1999/01/01: match
    ('1999', '01', '01')
    year: 1999
    
    1999.01.01: miss
    



```python
# As we add more groups, it can be confusing to 
# remember them by their positions, so we can name them with
# `?P<name>` just inside the parens
date_re = re.compile('(?P<year>\d{4})'
                     '[/-]'
                     '(?P<month>\d{2})'
                     '[/-]'
                     '(?P<day>\d{2})')

dates = ['1999-01-01', '1999/01/01', '1999.01.01']

for d in dates:
    match = date_re.match(d)
    print('{}: {}'.format(d, 'match' if match else 'miss'))
    if match:
        print('{} = year "{}" month "{}" day "{}"'.format(d, 
                                                          match.group('year'), 
                                                          match.group('month'), 
                                                          match.group('day')))
    print()
```

    1999-01-01: match
    1999-01-01 = year "1999" month "01" day "01"
    
    1999/01/01: match
    1999/01/01 = year "1999" month "01" day "01"
    
    1999.01.01: miss
    



```python
# What if we wanted to match a US phone number?
phone_re = re.compile('(\d{3})'  # area code
                      ' '        # a space
                      '\d{3}'    # prefix
                      '-'        # dash
                      '\d{4}')   # line number
phone_re.match('(800) 555-1212')
```


```python
# Why didn't that work?
# What do those parentheses do again? They group!
# So we need to indicate that the parens are literal 
# things to match by using backslashes `\` to escape them.
phone_re = re.compile('\('     # left paren
                      '\d{3}'  # area code
                      '\)'     # right paren
                      ' '      # space
                      '\d{3}'  # prefix
                      '-'      # dash
                      '\d{4}') # line number
phone_re.match('(800) 555-1212')
```




    <_sre.SRE_Match object; span=(0, 14), match='(800) 555-1212'>




```python
# We could also use character classes to make this more readable
phone_re = re.compile('[(]'    # left paren
                      '\d{3}'  # area code
                      '[)]'    # right paren
                      ' '      # space
                      '\d{3}'  # prefix
                      '-'      # dash
                      '\d{4}') # line number

phone_re.match('(800) 555-1212')
```




    <_sre.SRE_Match object; span=(0, 14), match='(800) 555-1212'>




```python
# There is not always a space after the area code, and it may 
# sometimes it may be more than one space (or a tab?)
# We can use the `\s` to indicate any type of whitespace and 
# `*` to indicate zero or more
phone_re = re.compile('[(]'    # left paren
                      '\d{3}'  # area code
                      '[)]'    # right paren
                      '\s*'    # zero or more spaces
                      '\d{3}'  # prefix
                      '-'      # dash
                      '\d{4}') # line number
phones = ['(800)555-1212', '(800) 555-1212', '(800)  555-1212']
for phone in phones:
    print('{}\t{}'.format(phone, phone_re.match(phone)))
```

    (800)555-1212	<_sre.SRE_Match object; span=(0, 13), match='(800)555-1212'>
    (800) 555-1212	<_sre.SRE_Match object; span=(0, 14), match='(800) 555-1212'>
    (800)  555-1212	<_sre.SRE_Match object; span=(0, 15), match='(800)  555-1212'>



```python
# When the parens around the area code are optional,
# usually there is a dash to separate the area code
phone_re = re.compile('[(]?'   # optional left paren
                      '\d{3}'  # area code
                      '[)]?'   # optional right paren
                      '[-]?'   # optional dash
                      '\s*'    # zero or more whitespace
                      '\d{3}'  # prefix
                      '-'      # dash
                      '\d{4}') # line number

phones = ['(800)555-1212', '(800) 555-1212', '800-555-1212']
for phone in phones:
    print('{}\t{}'.format(phone, phone_re.match(phone)))
```

    (800)555-1212	<_sre.SRE_Match object; span=(0, 13), match='(800)555-1212'>
    (800) 555-1212	<_sre.SRE_Match object; span=(0, 14), match='(800) 555-1212'>
    800-555-1212	<_sre.SRE_Match object; span=(0, 12), match='800-555-1212'>



```python
# This has the affect of matching a dash after parens which 
# is generally not a valid format
phone_re = re.compile('[(]?'
                      '\d{3}'
                      '[)]?'
                      '[-]?'
                      '\s*'
                      '\d{3}'
                      '-'
                      '\d{4}')

phone_re.match('(800)-555-1212')
```




    <_sre.SRE_Match object; span=(0, 14), match='(800)-555-1212'>




```python
# We really have to create two regexes to handle these cases
phone_re1 = re.compile('[(]'
                       '\d{3}'
                       '[)]'
                       '\s*'
                       '\d{3}'
                       '-'
                       '\d{4}')

phone_re2 = re.compile('\d{3}'
                       '-'
                       '\d{3}'
                       '-'
                       '\d{4}')

phones = ['(800)555-1212', '(800) 555-1212', '800-555-1212', '(800)-555-1212']
for phone in phones:
    match1 = phone_re1.match(phone)
    match2 = phone_re2.match(phone)
    print('{}\t{}'.format(phone, 'match' if match1 or match2 else 'miss'))
```

    (800)555-1212	match
    (800) 555-1212	match
    800-555-1212	match
    (800)-555-1212	miss



```python
# I worked with a graphic artist who always insisted on using 
# dots as the number separator, and sometimes there are no 
# separators at all. The combination of these two regexes find
# the valid formats and skip the invalid one.

phone_re1 = re.compile('[(]'
                       '\d{3}'
                       '[)]'
                       '\s*'
                       '\d{3}'
                       '[.-]'
                       '\d{4}')

phone_re2 = re.compile('\d{3}'
                       '[.-]?'
                       '\d{3}'
                       '[.-]?'
                       '\d{4}')

phones = ['8005551212', '(800)555-1212', '(800) 555-1212', 
          '800-555-1212', '(800)-555-1212', '800.555.1212']

for phone in phones:
    match = phone_re1.match(phone) or phone_re2.match(phone)
    print('{}\t{}'.format(phone, 'match' if match else 'miss'))
```

    8005551212	match
    (800)555-1212	match
    (800) 555-1212	match
    800-555-1212	match
    (800)-555-1212	miss
    800.555.1212	match



```python
# OK, now let's normalize the numbers by using parens to
# capture the area code, prefix, and line number and then 
# create a standard representation.
phone_re1 = re.compile('[(]'
                       '(\d{3})'  # group 1
                       '[)]'
                       '\s*'
                       '(\d{3})'  # group 2
                       '[.-]'
                       '(\d{4})') # group 3

phone_re2 = re.compile('(\d{3})'  # group 1
                       '[.-]?'
                       '(\d{3})'  # group 2
                       '[.-]?'
                       '(\d{4})') # group 3

phones = ['8005551212', '(800)555-1212', '(800) 555-1212', 
          '800-555-1212', '(800)-555-1212', '800.555.1212']

for phone in phones:
    match = phone_re1.match(phone) or phone_re2.match(phone)
    standard = '{}-{}-{}'.format(match.group(1), 
                                 match.group(2), 
                                 match.group(3)) if match else 'miss'
    print('{}\t{}'.format(phone, standard))
```

    8005551212	800-555-1212
    (800)555-1212	800-555-1212
    (800) 555-1212	800-555-1212
    800-555-1212	800-555-1212
    (800)-555-1212	miss
    800.555.1212	800-555-1212



```python
# And if we add named capture groups...
phone_re1 = re.compile('[(]'
                       '(?P<area_code>\d{3})'
                       '[)]'
                       '\s*'
                       '(?P<prefix>\d{3})'
                       '[.-]'
                       '(?P<line_num>\d{4})')

phone_re2 = re.compile('(?P<area_code>\d{3})'
                       '[.-]?'
                       '(?P<prefix>\d{3})'
                       '[.-]?'
                       '(?P<line_num>\d{4})')

phones = ['8005551212', '(800)555-1212', '(800) 555-1212', 
          '800-555-1212', '(800)-555-1212', '800.555.1212']

for phone in phones:
    match = phone_re1.match(phone) or phone_re2.match(phone)
    standard = '{}-{}-{}'.format(match.group('area_code'), 
                                 match.group('prefix'), 
                                 match.group('line_num')) if match else 'miss'
    print('{}\t{}'.format(phone, standard))
```

    8005551212	800-555-1212
    (800)555-1212	800-555-1212
    (800) 555-1212	800-555-1212
    800-555-1212	800-555-1212
    (800)-555-1212	miss
    800.555.1212	800-555-1212



```python
# And if we add named capture groups
# and named groups in `format` ...
phone_re1 = re.compile('[(]'
                       '(?P<area_code>\d{3})'
                       '[)]'
                       '\s*(?P<prefix>\d{3})'
                       '[.-]'
                       '(?P<line_num>\d{4})')
phone_re2 = re.compile('(?P<area_code>\d{3})'
                       '[.-]?'
                       '(?P<prefix>\d{3})'
                       '[.-]?'
                       '(?P<line_num>\d{4})')
phones = ['8005551212', '(800)555-1212', '(800) 555-1212', 
          '800-555-1212', '(800)-555-1212', '800.555.1212']
for phone in phones:
    match = phone_re1.match(phone) or phone_re2.match(phone)
    tmpl = '{area_code}-{prefix}-{line_num}'
    standard = tmpl.format(prefix=match.group('prefix'), 
                           area_code=match.group('area_code'),
                           line_num=match.group('line_num')) if match else 'miss'
    print('{}\t{}'.format(phone, standard))
```

    8005551212	800-555-1212
    (800)555-1212	800-555-1212
    (800) 555-1212	800-555-1212
    800-555-1212	800-555-1212
    (800)-555-1212	miss
    800.555.1212	800-555-1212



```python
# Write the regular expressions to parse the year, month, and
# day from the following date formats found in SRA metadata.
# When no day is present, e.g., "2/14," use "01" for the day.

d1 = "2012-03-09T08:59"
print(d1, re.match('', d1))

d2 = "2012-03-09T08:59:03"

d3 = "2017-06-16Z"

d4 = "2015-01"

d5 = "2015-01/2015-02"

d6 = "2015-01-03/2015-02-14" 

d7 = "20100910"

d8 = "12/06"

d9 = "2/14"

d10 = "2/14-12/15"

d11 = "2017-06-16Z"

# "Excel" format! What is that?! Look it up.
d12 = "34210"

d13 = "Dec-2015"

d14 = "March-2017"

d15 = "May, 2017"

d16 = "March-April 2017"

d17 = "July of 2011"

d18 = "2008 August"
```

    2012-03-09T08:59 <_sre.SRE_Match object; span=(0, 0), match=''>



```python
# Now combine all your code from the previous cell to normalize
# all the dates into the same format.

dates = ["2012-03-09T08:59", "2012-03-09T08:59:03", "2017-06-16Z", 
         "2015-01", "2015-01/2015-02", "2015-01-03/2015-02-14", 
         "20100910", "12/06", "2/14", "2/14-12/15", "2017-06-16Z", 
         "34210", "Dec-2015", "March-2017", "May, 2017", 
         "March-April 2017", "July of 2011", "2008 August"]

for date in dates:
    year = '1999'
    month = '01'
    day = '01'
    print('{}-{}-{}\t{}'.format(year, month, day, date))
```

    1999-01-01	2012-03-09T08:59
    1999-01-01	2012-03-09T08:59:03
    1999-01-01	2017-06-16Z
    1999-01-01	2015-01
    1999-01-01	2015-01/2015-02
    1999-01-01	2015-01-03/2015-02-14
    1999-01-01	20100910
    1999-01-01	12/06
    1999-01-01	2/14
    1999-01-01	2/14-12/15
    1999-01-01	2017-06-16Z
    1999-01-01	34210
    1999-01-01	Dec-2015
    1999-01-01	March-2017
    1999-01-01	May, 2017
    1999-01-01	March-April 2017
    1999-01-01	July of 2011
    1999-01-01	2008 August

