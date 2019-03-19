.PHONY: doc test

doc:
	pandoc README.md -o README.pdf --latex-engine=xelatex

test:
	python3 -m pytest -v test.py
