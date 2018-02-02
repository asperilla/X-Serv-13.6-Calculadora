#!/usr/bin/python3

import sys

if len(sys.argv) != 4:
	print("usage: <calculadora.py> <operacion> <operando1> <operando2>");
else:
	try:

		funcion = sys.argv[1];
		operando1 = float(sys.argv[2]);
		operando2 = float(sys.argv[3]);

		if funcion == 'suma':
			print(str(operando1 + operando2));
		elif funcion == 'resta':
			print(str(operando1 - operando2));
		elif funcion == 'multiplicacion':
			print(str(operando1 * operando2));
		elif funcion == 'division':
			try:
				print(str(operando1 / operando2));
			except ZeroDivisionError:
				print("No se puede dividir entre 0.");
				
		else:
			print("Las operaciones posibles son: suma, resta, multiplicacion o division");

	except ValueError:
		print("¡Operando1 y operando2 tienen que ser numeros!");

