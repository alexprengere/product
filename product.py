#!/usr/bin/env python

"""
Cartesian product with objective function to minimize.

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

"""


import heapq

__all__ = ["product"]


class UniqHeap:
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


class Grid:
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


def product(iterables, key=lambda x: x):
    grid = Grid([sorted(it, key=key) for it in iterables])
    try:
        heap = UniqHeap(key=lambda c: sum(key(v) for v in grid.get(c)))
        coords = grid.start

        while True:
            yield grid.get(coords)
            for n in grid.neighbors(coords):
                heap.push(n)
            coords = heap.pop()  # IndexError if empty

    except IndexError:
        pass


def main():
    import sys
    import doctest

    doctest.testmod()

    for t in product(sys.argv[1:], key=lambda x: 1):
        print(t)


if __name__ == "__main__":
    main()
