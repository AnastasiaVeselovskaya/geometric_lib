import pytest
import calculate


def test_calculate_wrong_input():
    with pytest.raises(ValueError, match="Figure 'cylinder' is not a valid figure."):
        figure_argument = 'cylinder'
        function_argument = 'area'
        size_argument = {3, 5}

        calculate.calc(figure_argument, function_argument, size_argument)


def test_calculate():
    figure_argument = 'square'
    function_argument = 'perimeter'
    size_argument = {9}

    result = calculate.calc(figure_argument, function_argument, size_argument)

    assert result == 36