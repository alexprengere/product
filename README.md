# product

Cartesian product with an objective function to minimize.
By default, the sum of returned elements.

```python
>>> from product import product
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

```

Now let's try with `sqrt` as objective function.
Note that `(1, 1)` is now after `(0, 2)` and `(2, 0)`.

```python
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

```

Change that to the square.
Note that `(1, 1)` is now before `(0, 2)` and `(2, 0)`.

```python
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

```
