#!/bin/bash

# Delete old build
rm -rf build dist > /dev/null

# Create new source and binary build
python3 setup.py sdist bdist_wheel

# Upload to PyPI
python3 -m twine upload dist/*
