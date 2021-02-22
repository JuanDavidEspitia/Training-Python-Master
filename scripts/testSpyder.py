# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 08:47:42 2021

@author: jespitiaa

"""
print("Hola Mundo")

nombre = input("Como te llamas? ")
print("Hola ", nombre)


def is_prime(number):
    """Return True if `number` is prime."""
    for element in range(2, number):
        if number % element == 0:
            return False
    return True


print(is_prime(9))

