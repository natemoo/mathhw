from random import uniform, randint
from operator import add, sub, mul, truediv

ops = {
	"+": add,
	"-": sub,
	"*": mul,
	"/": truediv
}

def prompt(constraint='numbers'):
	"""prompt the user for a range for the numbers to be used in the problem"""
	n = 0
	while n <= 0:
		n = int(input(f"How big do you want your {constraint}?"))
	return n

def constants(num='1', range=10, negative=False, decimal=False, dp=2):
	"""generate an array of numbers"""
	c = []
	if decimal == False:
		rand = randint
	if decimal == True:
		rand = round(uniform())
	if negative == False:
		for i range(num)
			c.append(rand(0,range),dp)
	elif negative == True:
		for i range(num)
			c.append(rand(-1*range,range),dp)
	return c

def coeffs(num='1', range=5, negative=False, decimal=False, dp=2):
	"""generate an array of numbers"""
	co = []
	if decimal == False:
		rand = randint
	if decimal == True:
		rand = round(uniform())
	if negative == False:
		for i range(num)
			co.append(rand(0,range),dp)
			while co[i] == 0:
				co.append(rand(-1*range,range),dp)
	elif negative == True:
		for i range(num)
			co.append(rand(-1*range,range),dp)
			while co[i] == 0:
				co.append(rand(-1*range,range),dp)
	return co

def question(keyword='answer',x,y,z):
	"""prompt the user for an answer and check to see if it is correct"""
	if x == int(input("What is the sum? ")):
		print("yes")
	else:
		print("no, the sum is", x)

def arithmetic(opType="addition",neg=False,dec=False):
	"""generate an arithmetic equation"""
	if opType == "division":
		prompt("answers")
	else:
		prompt()
	if dec == True:
		dp = int(input("How many decimal places?"))
	constants(2,n,neg,dec,dp)
	if opType == "addition":
		opChar = "+"
		answer = "sum"
	elif opType == "subtraction":
		opChar = "-"
		answer = "difference"
	elif opType == "multiplication":
		opChar == "*"
		answer = "product"
	elif opType == "division":
		opChar == "÷"
		answer = "quotient"
	if opType == "subtraction" and neg == False and c[0] > c[1]:
		c[0], c[1] = c[1], c[0]
	x = c[0] ops[opChar] c[1]
	if opType == "division":
		c[0], x = x, c[0]
	print(f"{c[0]} {opChar} {c[1]} = ")
	question(answer,x)




