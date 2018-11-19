from unittest import TestCase
from ipynb.fs.full.index import *

def test_add0(self):
    a = Point(x=None, y=None, a=5, b=7)
    b = Point(x=2, y=5, a=5, b=7)
    c = Point(x=2, y=-5, a=5, b=7)
    assert a+b == b
    assert b+a == b
    assert b+c == a