from overlap import oa

def test_basic():
    ''' Tests that basic example works '''
    big_field = (1, 1, 4, 4)
    inner_field = (2, 2, 3, 3)
    assert oa(big_field, inner_field) == 1
