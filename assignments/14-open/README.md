# Open Assignment

For this assignment, you are in charge! You will create a GitHub repository that will need to have:

1. `README.md`: A "read-me" file in Markdown format (Google it) like this file.
2. A Python program: You will decide what problem you need to solve and what it should be called.
3. `Makefile`: This should have at least a `test` target that documents how to run your tests. You can also include targets to run you program with various inputs.
4. `LICENSE`: I tend to choose MIT, but you need to decide how you intend others to reuse your code, if at all. Cf. Wilkinson et al 2016 (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4792175/)
5. `.gitignore`: This should list `__pycache__` and `.pytest_cache` directories along with any files you do not want committed to GitHub. Be esp sure to mention any large files (e.g., `.fa` FASTA input/output files) that could be downloaded and/or created by your program.

If you use the GitHub interface to start a new repo, you will be prompted to initialize the repo with a `README.md` and `LICENSE`.

Your `README.md` must contain:

1. The name and description of your program.
2. Examples of how to run the program and expected output
3. Description of how to run the tests.
4. Your full name and email address.

Optional files:

1. `README.pdf` *(optional)*: If you would like, learn how to install `pandoc` to convert Markdown to Latex and then PDF. See my Makefiles for examples of how to do this.
2. Inputs for tests or samples for demonstrations.
3. `test.py`: While you **must** have a test suite, it is not required to be in a separate file. If you wish, you can place your tests inside your Python program.

For your program, you might choose something from https://codingbat.com/java/Warmup-1 (I've started a few in the `warmups` directory that you can use for examples) or perhaps you want to encode some simple game. The problem itself can be inconsequential but it shouldn't be entirely trivial like "adding an `s` to a given input". Use your judgement and creativity!

The exercise is to push you to think about how you will approach a new project once you leave this course. Every new project I start begins with makingk a new GitHub repo. I generally do this via github.com, then `git clone` the new repo into my terminal, create new files, `git add/commit/push` them, etc. 

All of your code (program and tests) should be formatted with a standard tool like `black` or `yapf`. You should also check your code with something like `pylint`. Every function should have a docstring. If your program requires input files, either include small samples (e.g., FASTA/Q with just a few records) or instruction (or Make targets!) on how to download the necessary files.

Remember that this is a project that will live in your public GitHub repo. It will have your name on it and will serve as an example of how you write, verify, and document your code. A potential employer might one day look at this when deciding whether to hire you.  Make it shine!

# Test Coverage

If you are feeling ambitious, install and learn to use the `coverage` module (https://coverage.readthedocs.io/en/v4.5.x/) to see how well you have written your tests.

# Release

You will create a release tarball like "foo-0.0.1.tgz".