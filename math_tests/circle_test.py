import pytest
import circle

def test_circle_area():
    circle_radius = 12.0

    result = circle.area(circle_radius)

    assert result == pytest.approx(452.3893421169302, rel=1e-9)

def test_circle_perimeter():
    circle_radius = 6.0

    result = circle.perimeter(circle_radius)

    assert result == pytest.approx(37.69911184307752, rel=1e-9)