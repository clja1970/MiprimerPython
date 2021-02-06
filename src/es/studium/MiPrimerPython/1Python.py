#!/usr/bin/env python
# -- coding: utf-8 --
# 
#  format.py
#
'''
Created on 6 feb. 2021

@author: clja1
'''
print ("Vamos a sumar")
try:
    x=int(input ("introduce un número entero: "))
    y=int(input ("introduce otro número entero: "))
    def suma (x,y=0):
        return x+y
    print (("La suma es: ")+ str(suma(x, y)))
except ValueError:
    print("Números enteros por favor")





