.PHONY: doc test clean

test:
	python3 -m pytest -v test.py

clean:
	rm -rf __pycache__ .pytest_cache

doc:
	pandoc README.md -o README.pdf

