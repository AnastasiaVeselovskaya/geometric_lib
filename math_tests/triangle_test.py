import pytest
import triangle


def test_triangle_area():
    height = 6
    side = 45

    result = triangle.area(side, height)

    assert result == 135


def test_triangle_perimeter():
    side_a = 3
    side_b = 5
    side_c = 6

    result = triangle.perimeter(side_a, side_b, side_c)

    assert result == 14
