"""Tests for the calculation functions."""

from calc_funcs import add, subtract


def test_add_floats_rounds_to_2():

    res = add(0.1, 0.2)

    assert res == 0.3