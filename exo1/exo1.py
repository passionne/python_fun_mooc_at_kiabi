#!/usr/bin/env python
# -*- coding: utf-8 -*-

# fonction ( a, b, n ) qui retourne [n élement] qui est la suite de fibonacci à partir de a et b
# fonction (1, 2, 5) retourne [1, 2, 3, 5, 8]
# n = n-1 + n-2

import time

MAX_NUM_FIBO = 99999

def assertExpected(a, b):
    if a != b:
        raise AssertionError("ERROR : {0} != {1}".format(a, b))
    else:
        print "CHEKED : {0} == {1}".format(a, b)

#####
## Solution de Jérome
#####
def fibonacci_jerome(a, b, n):
    L=[]
    for i in range(n):
        L.append(a)
        a, b = b , a+b
    return L

assertExpected(fibonacci_jerome(1, 2, 2), [1, 2])
assertExpected(fibonacci_jerome(1, 2, 1), [1])
assertExpected(fibonacci_jerome(1, 2, 0), [])
assertExpected(fibonacci_jerome(1, 2, 5), [1, 2, 3, 5, 8])
assertExpected(fibonacci_jerome(2, 4, 4), [2, 4, 6, 10])

a, b = 2, 3
print a, b
print fibonacci_jerome(a, b, 3)
print a, b

start = time.time()
fibonacci_jerome(2, 4, MAX_NUM_FIBO)
end = time.time()
print("fibonacci_jerome : {0}".format(end - start))


#####
## Solution de Soda
#####
def fibonacci_soda(a, b, n):
    fibo=[a, b]
    l=len(fibo)
    if n==0:
        fibo=[]
    if n==1:
        fibo=[a]
    while l<n:
        new = fibo[-1] + fibo[-2]
        fibo.append(new)
        l=len(fibo)
    return fibo

assertExpected(fibonacci_soda(1, 2, 2), [1, 2])
assertExpected(fibonacci_soda(1, 2, 1), [1])
assertExpected(fibonacci_soda(1, 2, 0), [])
assertExpected(fibonacci_soda(1, 2, 5), [1, 2, 3, 5, 8])
assertExpected(fibonacci_soda(2, 4, 4), [2, 4, 6, 10])

start = time.time()
fibonacci_soda(2, 4, MAX_NUM_FIBO)
end = time.time()
print("fibonacci_soda : {0}".format(end - start))



#####
## Solution de Annie
#####
def fibonacci_annie(a, b, n):
    s=[a,b]
    for i in range(2,n) :
        s[i:i] = [s[i-1] + s[i-2]]
    return s[0:n]

assertExpected(fibonacci_annie(1, 2, 2), [1, 2])
assertExpected(fibonacci_annie(1, 2, 1), [1])
assertExpected(fibonacci_annie(1, 2, 0), [])
assertExpected(fibonacci_annie(1, 2, 5), [1, 2, 3, 5, 8])
assertExpected(fibonacci_annie(2, 4, 4), [2, 4, 6, 10])

start = time.time()
fibonacci_annie(2, 4, MAX_NUM_FIBO)
end = time.time()
print("fibonacci_annie : {0}".format(end - start))



#####
## Exercice de concatenation de chaine récursif
#####

def concat_n_fois(chaine, n):
    return concat_n_fois_accu(chaine, n, "", 1)

def concat_n_fois_accu(chaine, n, accu, acnum):
    accu = accu + chaine + str(acnum)
    if acnum<n:
        return concat_n_fois_accu(chaine, n, accu, acnum+1)
    else:
        return accu

assertExpected(concat_n_fois("x", 3), "x1x2x3")



#####
## fibonacci en mode recurcif
#####

def fibonacci_recur(a, b, n):
    if n==0:
        return []
    if n==1:
        return [a]
    return fibonacci_recur_accu(a, b, n-2, [a, b])


def fibonacci_recur_accu(a, b, n, accu):
    if n>0 :
        #print "cur : a={0} b={1} n={2} accu={3}".format(a, b, n, accu)
        next = a+b
        accu.append(next)
        return fibonacci_recur_accu(b, next, n-1, accu)
    else :
        return accu



assertExpected(fibonacci_recur(1, 2, 0), [])
assertExpected(fibonacci_recur(1, 2, 1), [1])
assertExpected(fibonacci_recur(1, 2, 2), [1, 2])
assertExpected(fibonacci_recur(1, 2, 5), [1, 2, 3, 5, 8])
assertExpected(fibonacci_recur(2, 4, 4), [2, 4, 6, 10])

start = time.time()
fibonacci_recur(2, 4, MAX_NUM_FIBO)
end = time.time()
print("fibonacci_recur : {0}".format(end - start))

