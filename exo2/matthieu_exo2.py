#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

####
#
#  Créer un fichier csv au format :
#   code article; libelle; prix; quantité
#
####

LIBELLE_BASE = ["robe", "veste", "chaussure", "chaussette"]
LIBELLE_COLOR = ["rouge", "bleu", "rose", "vert", "gris", "noir"]
LIBELLE_STYLE = ["stylé", "fashion", "for men", "girly"]

def generate_libelle():
    base = LIBELLE_BASE[random.randint(0, len(LIBELLE_BASE)-1)]
    color = LIBELLE_COLOR[random.randint(0, len(LIBELLE_COLOR)-1)]
    style = LIBELLE_STYLE[random.randint(0, len(LIBELLE_STYLE)-1)]
    return "{0} {1} {2}".format(base, color, style)


def generate_price():
    return "%.2f" % (random.random() + random.randint(1, 100))


def generate_quantite():
    return random.randint(1, 100)

def generate_code_article():
    return "{0}{1}{2}{3}{4}".format(random.choice('TFGLM'), random.choice('VLABM'), random.randint(0,9), random.randint(0,9), random.randint(0,9))

def generate_line():
    code_article = generate_code_article()
    libelle = generate_libelle()
    prix = generate_price()
    quantite = generate_quantite()
    return "{0};{1};{2};{3}".format(code_article, libelle, prix, quantite)


def generate_file(filename, nbLine):
    f = open(filename, 'w')
    f.write("code article;libelle;prix;quantité\n")
    for i in range(1, nbLine):
        f.write(generate_line())
        f.write("\n")
    f.close()

if __name__ == "__main__" :
    filename = "data1.csv"
    generate_file(filename, 10)

    for line in open(filename, 'r'):
        print(line[0:-1])
