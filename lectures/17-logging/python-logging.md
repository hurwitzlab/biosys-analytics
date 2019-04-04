# Logging in Python

So far we've use `print` statements that go to STDOUT and the `warn` function that makes is slightly more convenient to `print` to STDERR. The trouble with this approach to writing and debugging code is that you need to remove all the `print` statements prior to releasing your code or running your tests. With the `logging` module (https://docs.python.org/3/library/logging.html), you can sprinkle messages to yourself liberally throughout your code and chose *at run time* which ones to see. 

Like with `random.seed`, calls to the `logging` module affect the **global state** of how logging happens. First you need to set up how the logging will happen using the `basicConfig` (https://docs.python.org/3/library/logging.html#logging.basicConfig). Typically you will set log message to go to a `filename` in the default `filemode` of "a" (append) at some `level` like "debug":

````

````


The key is to understand the hierarchy of the levels:

1. CRITICAL
2. ERROR
3. WARNING
4. INFO
5. DEBUG
6. NOTSET

You