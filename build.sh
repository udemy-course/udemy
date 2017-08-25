#!/usr/bin/env bash

echo "pep8 check with flake8..."
flake8
echo "nosetests with coverage..."
nosetests --with-coverage --cover-erase --cover-package=udemy
echo "build sphinx doc..."
sphinx-build -d html docs/source docs/build

