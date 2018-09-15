from pytest import approx, raises
from hypothesis import given
from hypothesis.strategies import lists, integers, composite

from overlap import overlap_area

def test_basic():
    ''' Tests that basic example works '''
    big_field = (1, 1, 4, 4)
    inner_field = (2, 2, 3, 3)
    assert overlap_area(big_field, inner_field) == 1


def test_partial_overlap():
    ''' Tests when there's a partial overlap'''
    base_field = (1, 1, 4, 3)
    over_field = (2, 2, 3, 4)
    assert overlap_area(base_field, over_field) == 1


def test_corner_overlap():
    ''' Test when there is a box in a corner'''
    base_field = (1, 0, 3, 5)
    over_field = (2, 4, 4, 6)
    assert overlap_area(base_field, over_field) == 1


def test_edge_touching():
    ''' Test when there is an edge '''
    base_field = (1, 1, 4, 4)
    over_field = (2, 2, 3, 4)
    assert overlap_area(base_field, over_field) == 2


def test_2opposite_edge_touching():
    ''' Test when there is an edge '''
    base_field = (1, 1, 4, 4)
    over_field = (2, 1, 3, 4)
    assert overlap_area(base_field, over_field) == 3


def test_outside_edge_touching():
    ''' Test when they are touching on the outside '''
    base_field = (1, 1, 4, 4)
    over_field = (2, 4, 3, 5)
    assert overlap_area(base_field, over_field) == 0


def test_no_overlap():
    ''' Test when they are not touching each other '''
    base_field = (0, 0, 3, 3)
    over_field = (4, 4, 5, 5)
    assert overlap_area(base_field, over_field) == 0


def test_floats():
    ''' Test that still works when using floats '''
    base_field = (1, 1., 3.5, 3.5)
    over_field = (3, 3, 5, 5)
    assert overlap_area(base_field, over_field) == 0.5 * 0.5


def test_floats_again():
    ''' Test that still works when using floats '''
    base_field = (1, 1., 3.3, 3.1)
    over_field = (3, 3, 5, 5)
    assert overlap_area(base_field, over_field) == approx(0.3 * 0.1, rel=1e-3)


def test_negative_basic():
    ''' Tests that basic example works '''
    big_field = (-1, -1, -4, -4)
    inner_field = (-2, -2, -3, -3)
    with raises(ValueError, message=" Coordinates need to be entered (left, bottom, right, top) "):
        overlap_area(big_field, inner_field)


def test_negative_basic2():
    ''' Tests that basic example works '''
    big_field = (-1, -1, 1, 1)
    inner_field = (0, -2, 1, 2)
    assert overlap_area(big_field, inner_field) == 2


# Create a new strategy to use in our tests
@composite
def coordinates(draw, elements=integers()):
    xs = draw(lists(elements, min_size=4, max_size=4))
    xs[0], xs[2] = sorted([xs[0], xs[2]])
    xs[1], xs[3] = sorted([xs[1], xs[3]])
    return xs


@given(coordinates())
def test_full_inside(big_field):
    unit = 1
    # In case the field generated is of height or width 1.
    if big_field[2] - big_field[0] < 2 or big_field[3] - big_field[1] < 2:
        unit = -1

    other_field = [big_field[0] + unit, big_field[1] + unit,
                   big_field[2] - unit, big_field[3] - unit]

    # define which one is the inner field
    inner_field = other_field if unit == 1 else big_field
    area_inner = (inner_field[2] - inner_field[0]) * (inner_field[3] - inner_field[1])

    assert overlap_area(big_field, inner_field) == area_inner
