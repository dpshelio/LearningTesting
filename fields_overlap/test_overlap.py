import pytest
from pytest import approx, raises

from overlap import overlap_area

@pytest.mark.parametrize("big_field, inner_field, area", [
    ((1, 1, 4, 4), (2, 2, 3, 3), 1),
    ((1, 1, 4, 3), (2, 2, 3, 4), 1), # Tests when there's a partial overlap
    ((1, 0, 3, 5), (2, 4, 4, 6), 1), # Test when there is a box in a corner
    ((1, 1, 4, 4), (2, 2, 3, 4), 2), # Test when there is an edge
    ((1, 1, 4, 4), (2, 1, 3, 4), 3), # Test when there is an edge
    ((1, 1, 4, 4), (2, 4, 3, 5), 0), # Test when they are touching on the outside
    ((0, 0, 3, 3), (4, 4, 5, 5), 0), # Test when they are not touching each other
    ((1, 1., 3.5, 3.5), (3, 3, 5, 5), 0.5 * 0.5), # Test that still works when using floats
    ((1, 1., 3.3, 3.1), (3, 3, 5, 5), approx(0.3 * 0.1, rel=1e-3)), # Test that still works when using floats
    ((-1, -1, 1, 1), (0, -2, 1, 2), 2), # Tests that basic example works
])
def test_overlap_cases(big_field, inner_field, area):
    ''' Tests that basic example works '''
    assert overlap_area(big_field, inner_field) == area


def test_negative_basic():
    ''' Tests that basic example works '''
    big_field = (-1, -1, -4, -4)
    inner_field = (-2, -2, -3, -3)
    with raises(ValueError, message=" Coordinates need to be entered (left, bottom, right, top) "):
        overlap_area(big_field, inner_field)
