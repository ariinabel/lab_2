# Calculator Application

[![Python CI](https://github.com/<YOUR_USERNAME>/<YOUR_REPO>/actions/workflows/python.yml/badge.svg)](https://github.com/<YOUR_USERNAME>/<YOUR_REPO>/actions)
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](https://github.com/<YOUR_USERNAME>/<YOUR_REPO>/actions)

A simple calculator implementation with basic arithmetic operations.

## Features
- Addition
- Subtraction
- Multiplication
- Division (with zero-check)
- Exponentiation

## Installation
```bash
git clone https://github.com/<YOUR_USERNAME>/<YOUR_REPO>.git
cd <YOUR_REPO>

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

[![Documentation Status](https://github.com/<YOUR_USERNAME>/<YOUR_REPO>/actions/workflows/docs.yml/badge.svg)](https://<YOUR_USERNAME>.github.io/<YOUR_REPO>/)

## Documentation
Automatically generated documentation is published on [GitHub Pages](https://<YOUR_USERNAME>.github.io/<YOUR_REPO>/).

To build locally:
```bash
pip install -r requirements-dev.txt
mkdocs serve
