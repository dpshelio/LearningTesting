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
