#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Pair:
    max = 10
    nextVal = 0

    def __iter__(self):
        return self

    def next(self):
        raise StopIteration()


class Impair:
    max = 10
    cur = 0

    def __iter__(self):
        return self

    def next(self):
        raise StopIteration()


class Modulo:
    max = 10
    cur = 0
    mod = 0

    def __init__(self, mod):
        self.mod = mod

    def __iter__(self):
        return self

    def next(self):
        raise StopIteration()


assert [i for i in Pair()] == [0, 2, 4, 6, 8, 10]
assert [i for i in Impair()] == [0, 1, 3, 5, 7, 9, 11]
assert [i for i in Modulo(3)] == [0, 3, 6, 9, 12]
assert [i for i in Modulo(4)] == [0, 4, 8, 12]
