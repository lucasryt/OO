import pytest
from exercises.oo import Circle


def test_circle_attributes():
    c1 = Circle(10)
    assert hasattr(c1, 'radius')
    assert hasattr(c1, 'color')
    assert c1.radius == 10
    assert c1.color == 'red'

    c2 = Circle(10, 'blue')
    assert c1.radius == 10
    assert c1.color == 'blue'


def test_circle_methods():
    from math import pi

    c1 = Circle(10)
    assert c1.diameter() == 20
    assert abs(c1.area() - (100 * pi)) < 0.00001
