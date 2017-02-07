#!/usr/bin/python3

import sys

NUM_ARGS = 4

if len(sys.argv)!= NUM_ARGS:
	sys.exit("Usage: python3 calculadora.py operacion operando1 operando2")

_, operacion, operando1, operando2 = sys.argv
try:
	operando1 = float(operando1)
	operando2 = float(operando2)
except ValueError:
	print("Los operandos han de ser float")

if operacion == 'suma':
	print(operando1 + operando2)
elif operacion == 'resta' :
	print(operando1 - operando2)
elif operacion == 'multiplicacion' :
	print(operando1 * operando2)
elif operacion == 'division' :
	try:
		print(operando1 / operando2)
	except ZeroDivisionError:
		print("No se puede dividir entre 0")
else:
	print("Introduce una operacion del tipo: suma, resta, multiplicacion, division")
