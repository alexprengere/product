#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Cartesian product with objective function to minimize.

With no extra parameter, the minimized function relates to
the sum of the indices of the elements.

>>> for t in product([[0, 1, 2], [0, 1, 2]]):
...     print(t)
(0, 0)
(0, 1)
(1, 0)
(0, 2)
(1, 1)
(2, 0)
(1, 2)
(2, 1)
(2, 2)

Now let's try with sqrt as objective function to minimize.
Note that (1, 1) is now after (0, 2) and (2, 0).

>>> from math import sqrt
>>> for t in product([[0, 1, 2], [0, 1, 2]], key=sqrt):
...     print(t)
(0, 0)
(0, 1)
(1, 0)
(0, 2)
(2, 0)
(1, 1)
(1, 2)
(2, 1)
(2, 2)

Change that to the square.
Note that (1, 1) is now before (0, 2) and (2, 0).

>>> for t in product([[0, 1, 2], [0, 1, 2]], key=lambda i: i**2):
...     print(t)
(0, 0)
(0, 1)
(1, 0)
(1, 1)
(0, 2)
(2, 0)
(1, 2)
(2, 1)
(2, 2)
"""

from __future__ import with_statement, print_function, division

__all__ = ['product']


def neighbors(coords, limits):
    for i, limit in enumerate(limits):
        new_coords = list(coords)
        new_coords[i] += 1
        if new_coords[i] <= limit:
            yield tuple(new_coords)


def compute_next_coords(frontier, limits, f):
    candidates = []
    for coords in frontier:
        for n in neighbors(coords, limits):
            if n not in frontier:
                candidates.append(n)
    # This will raise ValueError and stop the process when done
    return min(candidates, key=f)


def clean(frontier, limits):
    """This keeps the frontier slim."""
    behind = set()
    for coords in frontier:
        if all(n in frontier for n in neighbors(coords, limits)):
            behind.add(coords)
    for coords in behind:
        frontier.remove(coords)


def get_values(iterables, coords):
    return tuple(it[c] for it, c in zip(iterables, coords))


def product(iterables, key=None):
    # The second element is to settle cases with equality
    # To make lesser coordinates a priority
    if key is None:
        f = lambda coords: (sum(coords), coords)
    else:
        for i, it in enumerate(iterables):
            iterables[i] = sorted(it, key=key)

        f = lambda coords: (sum(key(e) for e in get_values(iterables, coords)), \
                            coords)

    limits = tuple(len(it) - 1 for it in iterables)
    start_coords = tuple(0 for _ in iterables)
    yield get_values(iterables, start_coords)
    frontier = set([start_coords])

    while True:
        try:
            coords = compute_next_coords(frontier, limits, f)
            yield get_values(iterables, coords)
            frontier.add(coords)
            clean(frontier, limits)
        except ValueError:
            break


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    import sys
    for t in product(sys.argv[1:]):
        print(t)
