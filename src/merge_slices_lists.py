#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 3, 2014

@author: anroco

How merge a list with another using slices notation in python?

¿como unir una lista a otra usando notacion slices en python?
'''

#create a list
lista1 = [1, 4, 7, 3, 5, 2, 8, 6]
lista2 = [10, 13, 11, 14]
print (lista1)
print (lista2)


#merge a list with another defining the join index.
lista1[2:2] = lista2
print(lista1)

#create a list
lista2 = [21, 23, 27, 24, 28]
print (lista2)

#merge a list with another replacing some items of the list
lista1[8:11] = lista2
print(lista1)
