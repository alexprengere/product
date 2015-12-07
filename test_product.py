#!/usr/bin/env python
# -*- coding: utf-8 -*-

from product import product
from math import sqrt


def test_product():
    assert list(product([[0, 1, 2], [0, 1, 2]])) == [
        (0, 0),
        (0, 1),
        (1, 0),
        (0, 2),
        (1, 1),
        (2, 0),
        (1, 2),
        (2, 1),
        (2, 2),
    ]

    assert list(product([[0, 1, 2], [0, 1, 2]], key=sqrt)) == [
        (0, 0),
        (0, 1),
        (1, 0),
        (0, 2),
        (2, 0),
        (1, 1),
        (1, 2),
        (2, 1),
        (2, 2),
    ]

    assert list(product([[0, 1, 2], [0, 1, 2]], key=lambda i: i**2)) == [
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1),
        (0, 2),
        (2, 0),
        (1, 2),
        (2, 1),
        (2, 2),
    ]


def test_duplicatest():
    assert list(product([[2, 2], [2, 2]])) == [
        (2, 2),
        (2, 2),
        (2, 2),
        (2, 2),
    ]

