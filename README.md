# Calculator Application

[![Python CI](https://github.com/ariinabel/lab_2/actions/workflows/python.yml/badge.svg)](https://github.com/ariinabel/lab_2/actions)
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](https://github.com/ariinabel/lab_2/actions)

A simple calculator implementation with basic arithmetic operations.

## Features
- Addition
- Subtraction
- Multiplication
- Division (with zero-check)
- Exponentiation

## Installation
```bash
git clone https://github.com/ariinabel/lab_2.git
cd lab_2

## Usage

```python
from src.calculator import Calculator

calc = Calculator()
print(calc.add(2, 3))        # 5
print(calc.power(2, 3))      # 8
```

## Running tests

```bash
# Install dependencies
pip install -r requirements-dev.txt

# Run tests with coverage
pytest --cov=src --cov-report=term-missing tests/ -v
```

[![Documentation Status](https://github.com/ariinabel/lab_2/actions/workflows/docs.yml/badge.svg)](https://ariinabel.github.io/lab_2/)

## Documentation
Automatically generated documentation is published on [GitHub Pages](https://ariinabel.github.io/lab_2/).

To build locally:
```bash
pip install -r requirements-dev.txt
mkdocs serve
