# Pig Latin

Write a Python program named `piggie.py` that takes a positional argument that could be a filename or a bit of text and prints (to STDOUT) all the words in "Pig Latin" (see rules below).

Each word will need to have non-characters removed, e.g., with this expression:

````
import re
re.sub("[^a-zA-Z0-9']", '', word)
````

# Pig Latin Rules

1. If the word begins with consonants, e.g., "k" or "ch", move them to the end of the word and append "ay" so that "mouse" becomes "ouse-may" and "chair" becomes "air-chay."
2. If the word begins with a vowel, simple append "-yay" to the end, so "apple" is "apple-yay."

# Expected Output

````
$ ./piggie.py
usage: piggie.py [-h] STR
piggie.py: error: the following arguments are required: STR
$ ./piggie.py -h
usage: piggie.py [-h] STR

Convert to Pig Latin

positional arguments:
  STR         Input text or file

optional arguments:
  -h, --help  show this help message and exit
$ ./piggie.py 'Foo arf chaz!'
oo-Fay arf-yay az-chay
$ ./piggie.py inputs/nobody.txt
I'm-yay obody-Nay o-Whay are-yay ou-yay
Are-yay ou-yay -yay obody-Nay -yay oo-tay
en-Thay eres-thay a-yay air-pay of-yay us-yay
ont-Day ell-tay eyd-thay advertise-yay -yay ou-yay ow-knay

ow-Hay eary-dray -yay o-tay e-bay -yay omebody-Say
ow-Hay ublic-pay -yay ike-lay a-yay og-Fray -yay
o-Tay ell-tay one's-yay ame-nay -yay e-thay ivelong-lay une-Jay -yay
o-Tay an-yay admiring-yay og-Bay

````

# Test Suite

A passing test suite looks like this:

````
$ make test
pytest -v test.py
============================= test session starts ==============================
platform darwin -- Python 3.6.8, pytest-4.2.0, py-1.7.0, pluggy-0.8.1 -- /anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/kyclark/work/worked_examples/2019_spring_finals/piggie_a, inifile:
plugins: remotedata-0.3.1, openfiles-0.3.2, doctestplus-0.2.0, arraydiff-0.3
collected 6 items

test.py::test_usage PASSED                                               [ 16%]
test.py::test_text1 PASSED                                               [ 33%]
test.py::test_text2 PASSED                                               [ 50%]
test.py::test_nobody PASSED                                              [ 66%]
test.py::test_usdeclar PASSED                                            [ 83%]
test.py::test_gettysburg PASSED                                          [100%]

=========================== 6 passed in 0.46 seconds ===========================
````
