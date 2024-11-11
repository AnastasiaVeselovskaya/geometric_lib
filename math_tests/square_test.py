import pytest
import square

def test_square_area():
    square_side = 16

    result = square.area(square_side)

    assert result == 256

def test_square_perimeter():
    square_side = 34

    result = square.perimeter(square_side)

    assert result == 136