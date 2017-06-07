#!/usr/bin/env python
# -*- coding: utf-8 -*-

def found_unique(l):
    i = l[0]
    for j in l[1:]:
        i = i ^ j
    return i

assert found_unique([1,1,2,2,3,4,4,5,5]) == 3
assert found_unique([1,5,2,4,3,4,2,5,1]) == 3
assert found_unique([1,1,2,2,3,3,4,4,5]) == 5
assert found_unique([1,1,2,3,3,4,4,5,5]) == 2
