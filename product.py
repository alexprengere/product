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

Now let's try with an objective function to minimize.
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

import heapq
try:
    from itertools import izip as zip #pylint: disable=redefined-builtin
except ImportError:
    pass

__all__ = ['product']


class UniqHeap(object):
    def __init__(self, key=lambda x: x):
        self._key = key
        self._members = set()
        self._heap = []

    def push(self, item):
        if item not in self._members:
            self._members.add(item)
            heapq.heappush(self._heap, (self._key(item), item))

    def pop(self):
        item = heapq.heappop(self._heap)[1]
        self._members.remove(item)
        return item


class Grid(object):
    def __init__(self, iterables):
        self.iterables = iterables
        self.start = tuple(0 for _ in iterables)
        self.limits = tuple(len(it) - 1 for it in iterables)

    def get(self, coords):
        return tuple(it[c] for it, c in zip(self.iterables, coords))

    def neighbors(self, coords):
        for i, limit in enumerate(self.limits):
            neighbor = list(coords)
            neighbor[i] += 1
            if neighbor[i] <= limit:
                yield tuple(neighbor)


def product(iterables, key=None):
    for i, it in enumerate(iterables):
        iterables[i] = sorted(it, key=key)

    grid = Grid(iterables)
    if key is None:
        f = sum
    else:
        f = lambda coords: sum(key(v) for v in grid.get(coords))

    try:
        heap = UniqHeap(key=f)
        coords = grid.start

        while True:
            yield grid.get(coords)
            for n in grid.neighbors(coords):
                heap.push(n)
            coords = heap.pop() # IndexError if empty

    except IndexError:
        pass


def main():
    import sys
    import doctest

    doctest.testmod()

    for t in product(sys.argv[1:]):
        print(t)


if __name__ == '__main__':
    main()

