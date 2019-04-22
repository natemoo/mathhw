from random import uniform, randint
from operator import add, sub, mul, truediv
from math import sqrt

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

def constants(num=2, conRange=10, negative=False, decimal=False, dp=2):
	"""generate an array of numbers"""
	c = []
	for i in range(num):
		if decimal == False:
			if negative == False:
				rand = randint(0,conRange)
			elif negative == True:
				rand = randint(-1*conRange,conRange)
		if decimal == True:
			if negative == False:
				rand = round(uniform(0,conRange),dp)
			elif negative == True:
				rand = round(uniform(-1*conRange,conRange),dp)
		c.append(rand)
	return c

def coeffs(num=2, coeffRange=10, negative=True, decimal=False, dp=2):
	"""generate an array of numbers"""
	co = []
	for i in range(num):
		co.insert(i,0)
		while co[i] == 0:
			if decimal == False:
				if negative == False:
					rand = randint(0,coeffRange)
				elif negative == True:
					rand = randint(-1*coeffRange,coeffRange)
			if decimal == True:
				if negative == False:
					rand = round(uniform(0,coeffRange),dp)
				elif negative == True:
					rand = round(uniform(-1*coeffRange,coeffRange),dp)
			co[i] = rand
	return co

def question(keyword='the answer',x=0.0, y=None, z=None):
	"""prompt the user for an answer and check to see if it is correct"""
	userAnswer = input(f"What is {keyword}? ")
	try:
		if x == int(userAnswer):
			print("yes")
			if y:
				if y == int(input("What is y?")):
					print("yes")
				else:
					print(f"no, y is {y}")
		else:
			print(f"no, {keyword} is {x}")
	except ValueError:
		if x == float(userAnswer):
			print("yes")
		else:
			print(f"no, {keyword} is {x}")

def arithmetic(opType="addition",neg=False,dec=False):
	"""generate an arithmetic equation"""
	if opType == "division":
		n = prompt("answers")
	else:
		n = prompt()
	if dec == True:
		dp = int(input("How many decimal places?"))
	else:
		dp = False
	c = constants(2,n,neg,dec,dp)
	if opType == "addition":
		opChar = "+"
		answer = "sum"
	elif opType == "subtraction":
		opChar = "-"
		answer = "difference"
	elif opType == "multiplication":
		opChar = "*"
		answer = "product"
	elif opType == "division":
		opChar = "/"
		answer = "quotient"
		while c[0] == 0:
			c = constants(2,n,neg,dec,dp)
		while c[1] == 0:
			c = constants(2,n,neg,dec,dp)
	if opType == "subtraction" and neg == False and c[0] < c[1]:
		c[0], c[1] = c[1], c[0]
	opFun = ops[opChar]
	if opType == "division":
		x = c[0]*c[1]
	else:
		x = opFun(c[0], c[1])
	if opType == "division":
		c[0], x = x, c[0]
	print(f"{c[0]} {opChar} {c[1]} = ")
	question(f'the {answer}',x)

class binomial:
	def __init__(self, xcoefficient=randint(1,5), constantterm=randint(-10,10)):
		self.xcoefficient = xcoefficient
		self.constantterm = constantterm
		self.solution = -1*constantterm / xcoefficient
	
	def expression(self):
		print(f"{self.xcoefficient}x + {self.constantterm}")

class trinomial:
	def __init__(self, factor1, factor2):
		self.factor1 = factor1
		self.factor2 = factor2
		self.x2coefficient = factor1.xcoefficient * factor2.xcoefficient
		self.xcoefficient = factor1.xcoefficient * factor2.constantterm + factor1.constantterm * factor2.xcoefficient
		self.constantterm = factor1.constantterm * factor2.constantterm
		self.solution = (-1*self.xcoefficient + sqrt(self.xcoefficient**2-4*self.x2coefficient*self.constantterm))/(2*self.x2coefficient)

	def expression(self):
		print(f"{self.x2coefficient}x^2 + {self.xcoefficient}x + {self.constantterm}")

