# product

Cartesian product with objective function to minimize.

With no extra parameter, the minimized function relates to
the sum of the indices of the elements.

```python
>>> for t in product([[0, 1, 2], [0, 1, 2]]):
...     print t
(0, 0)
(0, 1)
(1, 0)
(0, 2)
(1, 1)
(2, 0)
(1, 2)
(2, 1)
(2, 2)
```

Now let's try with sqrt as objective function to minimize.
Note that (1, 1) is now after (0, 2) and (2, 0).

```python
>>> from math import sqrt
>>> for t in product([[0, 1, 2], [0, 1, 2]], key=sqrt):
...     print t
(0, 0)
(0, 1)
(1, 0)
(0, 2)
(2, 0)
(1, 1)
(1, 2)
(2, 1)
(2, 2)
```

Change that to the square.
Note that (1, 1) is now before (0, 2) and (2, 0).

```python
>>> for t in product([[0, 1, 2], [0, 1, 2]], key=lambda i: i**2):
...     print t
(0, 0)
(0, 1)
(1, 0)
(1, 1)
(0, 2)
(2, 0)
(1, 2)
(2, 1)
(2, 2)
```
