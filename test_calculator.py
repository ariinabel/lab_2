import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_addition(calc, a, b, expected):
    assert calc.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (7, 2, 5),
    (10, 10, 0),
    (-1, -1, 0),
])
def test_subtraction(calc, a, b, expected):
    assert calc.subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 12),
    (0, 5, 0),
    (-2, 3, -6),
])
def test_multiplication(calc, a, b, expected):
    assert calc.multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5.0),
    (9, 3, 3.0),
    (1, 2, 0.5),
])
def test_division(calc, a, b, expected):
    assert calc.divide(a, b) == expected

def test_division_by_zero(calc):
    with pytest.raises(ValueError) as excinfo:
        calc.divide(5, 0)
    assert "Cannot divide by zero" in str(excinfo.value)

@pytest.mark.parametrize("base, exponent, expected", [
    (2, 3, 8),
    (5, 0, 1),
    (10, 1, 10),
    (2, -1, 0.5),
])
def test_power(calc, base, exponent, expected):
    assert calc.power(base, exponent) == expected
