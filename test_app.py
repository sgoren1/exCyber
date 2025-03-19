from main import add
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (1.5, 2.5, 4.0),
    (-2, -3, -5)
])
def test_add(a, b, expected):
    assert add(a, b) == expected