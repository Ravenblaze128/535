from typing import Literal
import pytest
from MathUtils import MathUtils

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 15),
    (-1, -1, -2),
    (0, 0, 0)
])
def test_add(a: Literal[10, -1, 0], b: Literal[5, -1, 0], expected: Literal[15, -2, 0]):
    assert MathUtils.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 5),
    (-1, 1, -2),
    (0, 0, 0)
])
def test_subtract(a: Literal[10, -1, 0], b: Literal[5, 1, 0], expected: Literal[5, -2, 0]):
    assert MathUtils.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 50),
    (-1, -1, 1),
    (0, 0, 0)
])
def test_multiply(a: Literal[10, -1, 0], b: Literal[5, -1, 0], expected: Literal[50, 1, 0]):
    assert MathUtils.multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5.0),
    (-4, 2, -2.0),
    (0, 1, 0.0),
    (5, 0, -1.0)  # Testing division by zero
])
def test_divide(a: Literal[10, -4, 0, 5], b: Literal[2, 1, 0], expected: float):
    assert MathUtils.divide(a, b) == expected
