#!/usr/bin/python
# -*- coding: utf-8 -*-

def calcula(operacion, var1, var2):
    if operacion == 'sumar':
        return var1 + var2
    elif operacion == 'restar':
        return var1 - var2
    elif operacion == 'multiplicar':
        return var1 * var2
    elif operacion == 'dividir':
        try:
            return var1 / var2
        except ZeroDivisionError:
            sys.exit('No se puede dividir entre 0')


import sys

entradas = sys.argv
print entradas

operacion = entradas[1]

try:
    var1 = float(entradas[2])
    var2 = float(entradas[3])
except ValueError:
    sys.exit('Has introducido un operando no numérico')
except IndexError:
    sys.exit('Faltan operandos')

operaciones = ['sumar', 'restar', 'multiplicar', 'dividir']

if operacion in operaciones:
    salida = calcula(operacion,var1,var2)
    print 'El resultado de', operacion, var1, 'y', var2, 'es igual a', salida
else:
    sys.exit('La operación que has pedido no es válida')

