#!/usr/bin/env python3

print ("Calculator\n")

while True:
	number_1 = int(input("Type first number: "))
	op_value = input("Type operation (+, -, *, /): ")
	number_2 = int(input("Type second number: "))

	if (op_value == '+'):
		print ("{} + {} = {}".format(number_1, number_2, number_1 + number_2))
	elif (op_value == '-'):
		print ("{} - {} = {}".format(number_1, number_2, number_1 - number_2))
	elif (op_value == '*'):
		print ("{} * {} = {}".format(number_1, number_2, number_1 * number_2))
	elif (op_value == '/'):
		print ("{} / {} = {}".format(number_1, number_2, number_1 / number_2))
	else:
		print ("Invalid operation")
