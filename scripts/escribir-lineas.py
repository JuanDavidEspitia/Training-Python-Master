# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 08:57:57 2021

@author: jespitiaa
"""

import sys

if len(sys.argv) == 3:
	texto = sys.argv[1]
	repeticiones = int(sys.argv[2])
	for r in range(repeticiones):
		print(texto)
else:
	print("Error - Introduce los argumentos correctamente")
	print('Ejemplo: escribir_lineas.py "Texto" 5')
    
    