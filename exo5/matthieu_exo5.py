#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Pair:
    max = 10
    cur = 0

    def __iter__(self):
        return self

    def next(self):
        if self.cur < self.max:
            self.cur += 2
        else :
            raise StopIteration()
        return self.cur


class Impair:
    max = 11
    cur = 1

    def __iter__(self):
        return self

    def next(self):
        while self.cur < self.max:
            print(self.cur)
            yield self.cur
            self.cur += 2
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


if __name__ == "__main__" :
    assert [i for i in Pair()] == [2, 4, 6, 8, 10]
    assert [i for i in Impair()] == [1, 3, 5, 7, 9, 11]
    assert [i for i in Modulo(3)] == [3, 6, 9, 12]
    assert [i for i in Modulo(4)] == [4, 8, 12]
