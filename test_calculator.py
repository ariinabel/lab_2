import pytest
from calculator import Calculator

def test_addition_and_subtraction():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.subtract(7, 2) == 5

def test_multiplication_and_division():
    calc = Calculator()
    assert calc.multiply(3, 4) == 12
    assert calc.divide(10, 2) == 5.0

def test_division_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError) as excinfo:
        calc.divide(5, 0)
    assert "Cannot divide by zero" in str(excinfo.value)
