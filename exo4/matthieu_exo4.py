#!/usr/bin/env python
# -*- coding: utf-8 -*-

trad = {
    "FR": "Bonjour",
    "EN": "Hello",
    "ES": "Ola"
}

def sayHello(countryCode, firstname):
    return "{} {}!".format(trad[countryCode], firstname)

if __name__ == "__main__" :
    assert sayHello("FR", "jack") == "Bonjour jack!"
    assert sayHello("EN", "alice") == "Hello alice!"
    assert sayHello("ES", "bob") == "Ola bob!"

    print("Done")
