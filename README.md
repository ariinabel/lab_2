# Calculator Application

[![CI status](https://github.com/ariinabel/lab_2/actions/workflows/test-and-docs.yaml/badge.svg)](https://github.com/ariinabel/lab_2/actions/workflows/test-and-docs.yaml)

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

[![Generated Documentation Status](https://github.com/ariinabel/lab_2/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/ariinabel/lab_2/actions/workflows/pages/pages-build-deployment)

## Documentation
Automatically generated documentation is published on [GitHub Pages](https://ariinabel.github.io/lab_2/).

To build locally:
```bash
pip install -r requirements-dev.txt
mkdocs serve
