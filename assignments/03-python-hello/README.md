# Hello, Python!

Write a Python program named "hello.py" that warmly greets the names you provide.  When there are two names, join them with "and."  When there are three or more, join them on commas (INCLUDING THE OXFORD WE ARE NOT SAVAGES) and "and." If no names are supplied, print a usage:

```
$ ./hello.py
Usage: hello.py NAME [NAME2 ...]
$ ./hello.py Alice
Hello to the 1 of you: Alice!
$ ./hello.py Mike Carol
Hello to the 2 of you: Mike and Carol!
$ ./hello.py Greg Peter Bobby Marcia Jane Cindy
Hello to the 6 of you: Greg, Peter, Bobby, Marcia, Jane, and Cindy!
```

Your program needs to:

* Check the number of arguments
* If there are no arguments, print a "Usage" and exit with an error
* print "Hello to the N of you: ...!" where "N" is the number of arguments and "..." is the properly formatted as shown above for 1, 2, or >2 arguments

Think about how you solved these problems in bash:

* How do you find the number of arguments to your program?
* How do you print a usage statement?
* How do you exit with an error?
* How do you check for a condition, e.g., I have just one argument?
* How do you check for a second condition, e.g., I have two arguments?
* How do you check for a third/final condition, e.g., I have more than two arguments?
* How do you inspect the methods that Python lists have?

# Vowel Counter

Write a Python program called "vowel_counter.py" that counts the number of vowels in a single string. Be sure your subject and verb agree in number, and use proper plurals.

```
$ ./vowel_counter.py
Usage: vowel_counter.py STRING
$ ./vowel_counter.py for
There is 1 vowel in "for."
$ ./vowel_counter.py elliptical
There are 4 vowels in "elliptical."
$ ./vowel_counter.py YYZ
There are 0 vowels in "YYZ."
```

Your program needs to:

* Check the number of arguments
* If there is not one argument, print a "Usage" and exit with an error
* Count the number of vowels (case-insensitive) and print a grammatically correct sentence reporting the number

You can solve this exercise in many ways.  For example, you could use a `for` loop that iterates over a list of vowels and counts how many times that vowels occurs in the word you were given.  (Hint: there is a method in the `str` class that will do exactly this!)  Here is some pseudo-code:

```
create a variable to hold the count
for vowels in vowels:
    how often does vowel occur in word?
    add that number to the count
```

# Tests

A successful test suite looks like this:

```
$ make test
python3 -m pytest -v test.py
============================= test session starts ==============================
platform darwin -- Python 3.7.0, pytest-3.8.0, py-1.6.0, pluggy-0.7.1 -- /anaconda3/bin/python3
cachedir: .pytest_cache
rootdir: /Users/kyclark/work/worked_assignments/03-python-hello, inifile:
plugins: remotedata-0.3.0, openfiles-0.3.0, doctestplus-0.1.3, arraydiff-0.2
collected 5 items

test.py::test_exists PASSED                                              [ 20%]
test.py::test_usage PASSED                                               [ 40%]
test.py::test_hello PASSED                                               [ 60%]
test.py::test_counter PASSED                                             [ 80%]
test.py::test_tictactoe PASSED                                           [100%]

=========================== 5 passed in 0.39 seconds ===========================
```

# Grading

All tests must pass to receive credit.
