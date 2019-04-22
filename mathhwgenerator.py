from random import uniform, randint

# Prompt the user for a task
# Tasks currently supported:
# Arithmetic with whole numbers, integers, fractions, and decimals
# onestep (one step equations)
# twostep (two step equations)
# distprop (distributive property equations)
# simpbothsides (simple equations with variables on both sides)
# distbothsides (equations using the distributive property with variables on both sides)
# quadratic (quadratic equation with real solutions; broken for fractions)
task = input("What do you want to do?")

# Section: Arithmetic
# Whole number arithmetic
if task == "add":
	n = 0
	while n <= 0:
		n = int(input("How big do you want your numbers?"))
	n = int(n)
	m = randint(0,n)
	n = randint(0,n)
	x = m + n
	print(m, "+", n, "=")
	if x == int(input("What is the sum? ")):
		print("yes")
	else:
		print("no, the sum is", x)

elif task == "subtract":
	n = 0
	while n <= 0:
		n = int(input("How big do you want your numbers?"))
	n = int(n)
	m = randint(0,n)
	n = randint(0,n)
	if m > n:
		x = m - n
		print(m, "-", n, "=")
		if x == int(input("What is the difference? ")):
			print("yes")
		else:
			print("no, the difference is", x)
	else:
		x = n - m
		print(n, "-", m, "=")
		if x == int(input("What is the difference? ")):
			print("yes")
		else:
			print("no, the difference is", x)

elif task == "multiply":
	n = 0
	while n <= 0:
		n = int(input("How big do you want your numbers?"))
	n = int(n)
	m = randint(0,n)
	n = randint(0,n)
	x = m * n
	print(m, "*", n, "=")
	if x == int(input("What is the product? ")):
		print("yes")
	else:
		print("no, the product is", x)

elif task == "divide":
	n = 0
	while n <= 0:
		n = int(input("How big do you want your answers?"))
	n = int(n)
	m = randint(0,n)
	x = randint(0,n)
	n = x*m
	print(n, "/", m, "=")
	if x == int(input("What is the quotient? ")):
		print("yes")
	else:
		print("no, the quotient is", x)

# Integer Arithmetic
elif task == "addneg":
	n = 0
	while n <= 0:
		n = int(input("How big do you want your numbers?"))
	n = int(n)
	m = randint(-1*n,n)
	n = randint(-1*n,n)
	x = m + n
	print(m, "+", n, "=")
	if x == int(input("What is the sum? ")):
		print("yes")
	else:
		print("no, the sum is", x)

elif task == "subtractneg":
	n = 0
	while n <= 0:
		n = int(input("How big do you want your numbers?"))
	n = int(n)
	m = randint(-1*n,n)
	n = randint(-1*n,n)
	x = m - n
	print(m, "-", n, "=")
	if x == int(input("What is the difference? ")):
		print("yes")
	else:
		print("no, the difference is", x)

elif task == "multiplyneg":
	n = 0
	while n <= 0:
		n = int(input("How big do you want your numbers?"))
	n = int(n)
	m = randint(-1*n,n)
	n = randint(-1*n,n)
	x = m * n
	print(m, "*", n, "=")
	if x == int(input("What is the product? ")):
		print("yes")
	else:
		print("no, the product is", x)

elif task == "divideneg":
	n = 0
	while n <= 0:
		n = int(input("How big do you want your answers?"))
	n = int(n)
	m = randint(-1*n,n)
	x = randint(-1*n,n)
	n = x*m
	print(n, "/", m, "=")
	if x == int(input("What is the quotient? ")):
		print("yes")
	else:
		print("no, the quotient is", x)

# Fraction arithmetic
elif task == "addfract":
	n = 0
	while n <= 0:
		n = int(input("How big do you want your numbers?"))
	n = int(n)
	m1 = randint(0,n)
	m2 = randint(0,n)
	if m1 > m2:
		m1,m2=m2,m1
	m0 = m1/m2
	n1 = randint(0,n)
	n2 = randint(0,n)
	if n1 > n2:
		n1,n2=n2,n1
	n0 = n1/n2
	x = m0 + n0
	print(m1, "/", m2, "+", n1, "/", n2, "=")
#need to fix fraction answers
	if x == float(input("What is the sum? ")):
		print("yes")
	else:
		print("no, the sum is", x)

elif task == "subtractfract":
	n = 0
	while n <= 0:
		n = int(input("How big do you want your numbers?"))
	n = int(n)
	m1 = randint(0,n)
	m2 = randint(0,n)
	if m1 > m2:
		m1,m2=m2,m1
	m0 = m1/m2
	n1 = randint(0,n)
	n2 = randint(0,n)
	if n1 > n2:
		n1,n2=n2,n1
	n0 = n1/n2
	if m0 > n0:
		x = m0 - n0
		print(m1, "/", m2, "-", n1, "/", n2, "=")
	else:
		x = n0 - m0
		print(n1, "/", n2, "-", m1, "/", m2, "=")
	if x == float(input("What is the difference? ")):
		print("yes")
	else:
		print("no, the difference is", x)

elif task == "multiplyfract":
	n = 0
	while n <= 0:
		n = int(input("How big do you want your numbers?"))
	n = int(n)
	m1 = randint(0,n)
	m2 = randint(0,n)
	if m1 > m2:
		m1,m2=m2,m1
	m0 = m1/m2
	n1 = randint(0,n)
	n2 = randint(0,n)
	if n1 > n2:
		n1,n2=n2,n1
	n0 = n1/n2
	x = m0 * n0
	print(m1, "/", m2, "*", n1, "/", n2, "=")
#need to fix fraction answers
	if x == float(input("What is the product? ")):
		print("yes")
	else:
		print("no, the product is", x)

elif task == "dividefract":
	n = 0
	while n <= 0:
		n = int(input("How big do you want your answers?"))
	n = int(n)
	m1 = randint(0,n)
	m2 = randint(0,n)
	if m1 > m2:
		m1,m2=m2,m1
	m0 = m1/m2
	x1 = randint(0,n)
	x2 = randint(0,n)
	if x1 > x2:
		n1,n2=n2,n1
	x = x1/x2
	n0 = m0 * x
#how to convert decimal to fraction
	print(m1, "/", m2, "÷", n0, "=")
#need to fix fraction answers
	if x == float(input("What is the quotient? ")):
		print("yes")
	else:
		print("no, the quotient is", x)

# Decimal arithmetic
if task == "adddec":
	n = 0
	while n <= 0:
		n = int(input("How big do you want your numbers?"))
	n = int(n)
	dp = int(input("How many decimal places?"))
	m = round(uniform(0,n), dp)
	n = round(uniform(0,n), dp)
	x = m + n
	print(m, "+", n, "=")
	if x == float(input("What is the sum? ")):
		print("yes")
	else:
		print("no, the sum is", x)

elif task == "subtractdec":
	n = 0
	while n <= 0:
		n = int(input("How big do you want your numbers?"))
	n = int(n)
	dp = int(input("How many decimal places?"))
	m = round(uniform(0,n), dp)
	n = round(uniform(0,n), dp)
	if m > n:
		x = m - n
		print(m, "-", n, "=")
		if x == float(input("What is the difference? ")):
			print("yes")
		else:
			print("no, the difference is", x)
	else:
		x = n - m
		print(n, "-", m, "=")
		if x == int(input("What is the difference? ")):
			print("yes")
		else:
			print("no, the difference is", x)

elif task == "multiplydec":
	n = 0
	while n <= 0:
		n = int(input("How big do you want your numbers?"))
	n = int(n)
	dp = int(input("How many decimal places?"))
	m = round(uniform(0,n), randint(0,dp))
	n = round(uniform(0,n), randint(0,dp))
	x = m * n
	print(m, "*", n, "=")
	if x == float(input("What is the product? ")):
		print("yes")
	else:
		print("no, the product is", x)

elif task == "dividedec":
	n = 0
	while n <= 0:
		n = int(input("How big do you want your answers?"))
	n = int(n)
	dp = int(input("How many decimal places?"))
	m = round(uniform(0,n), dp)
	x = round(uniform(0,n), dp)
	n = x*m
	print(n, "/", m, "=")
	if x == float(input("What is the quotient? ")):
		print("yes")
	else:
		print("no, the quotient is", x)

# Section: Algebra

# These tasks all have simple solutions (integers for linear equations and real numbers for quadratics)

# Generate a onestep equation

elif task == "onestep":
	n = 0
	while n <= 0:
		n = int(input("How big do you want your numbers?"))
	n = int(n)
	x = randint(-1*n,n)
	a = randint(-1*n,n)
	while a == 0:
		a = randint(-1*n,n)
	s = randint(1,4)
	if s == 1:
		b = a*x
		print(a, "x =", b)
	elif s == 2:
		b = x/a
		print("x/", a, "=", b)
	elif s == 3:
		b = x + a
		print("x +", a, "=", b)
	elif s == 4:
		b = x - a
		print("x -", a, "=", b)
	if x == int(input("What is x?")):
		print("yes")

# Generate a two step equation

elif task == "twostep":
	n = 0
	while n <= 0:
		n=int(input("How big do you want your numbers?"))
	n = int(n)
	x = randint(-1*n,n)
	a = randint(-1*n,n)
	while a == 0:
		a = randint(-1*n,n)
	a2 = randint(-1*n,n)
	s = randint(1,2)
	if s == 1:
		b = a*x+a2
		print(a, "x +", a2, "=", b)
	elif s == 2:
		b = a*x-a2
		print(a,"x -", a2, "=", b)
	if x == int(input("What is x?")):
		print("yes")

# Generate a distributive property equation

elif task == "distprop":
	n = 0
	while n <= 0:
		n=int(input("How big do you want your numbers?"))
	x = randint(-1*n,n)
	a = randint(-1*n,n)
	a2 = randint(-1*n,n)
	while a2 == 0:
		a2 = randint(-1*n,n)
	a3 = randint(-1*n,n)
	while a3 == 0:
		a3 = randint(-1*n,n)
	a4 = randint(-1*n,n)
	s = randint(1,2)
	if s == 1:
		b = a + a2*a3*x+a2*a4
		print(a, "+", a2, "(", a3, "x +", a4, ") =", b)
	elif s == 2:
		b = a*x + a2*a3*x+a2*a4
		print(a, "x +", a2, "(", a3, "x +", a4, ") =", b)
	if x == int(input("What is x?")):
		print("yes")
	else:
		print("no")

# Generate an equation with variables on both sides in the form ax + b = cx + d

elif task == "simpbothsides":
	n = 0
	while n <= 0:
		n=int(input("How big do you want your numbers?"))
	x = randint(-1*n,n)
	a = randint(-1*n,n)
	while a == 0:
		a = randint(-1*n,n)
	a2 = randint(-1*n,n)
	a3 = randint(-1*n,n)
	while a3 == 0 or a3 == -1*a:
		a3 = randint(-1*n,n)
#	s = randint(1,4)
#	if s == 1:
	a4 = a*x+a2-a3*x
	print(a, "x +", a2, "=", a3, "x +", a4)
#	if s == 2:
#		a4 = x/a+a2-a3*x
#		print("x/", a, "+", a2, "=", a3, "x +", a4)
#	if s == 3:
#		a4 = x/a+a2-x/a3
#		print("x/", a, "+", a2, "=", "x/", a3, "+", a4)
#	if s == 4:
#		a4 = x/a-a3*x
#		print("x/", a, "=", a3, "x +", a4)
	if x == int(input("What is x?")):
		print("yes")
	else:
		print("no")

# Generate an equation with variables on both sides using the distributive property

elif task == "distbothsides":
	n = 0
	while n <= 0:
		n=int(input("How big do you want your numbers?"))
	x = randint(-1*n,n)
	a = randint(-1*n,n)
	while a == 0:
		a = randint(-1*n,n)
	a2 = randint(-1*n,n)
	while a2 == 0:
		a2 = randint(-1*n,n)
	a3 = randint(-1*n,n)
	a4 = randint(-1*n,n)
	a5 = randint(-1*n,n)
	while a5 == 0:
		a5 = randint(-1*n,n)
	a6 = randint(-1*n,n)
	while a6 == 0 or a6 == -1*a*a2/a5:
		a6 = randint(-1*n,n)
	a7 = randint(-1*n,n)
	a8 = a*a2*x+a*a3+a4-a5*a6*x-a5*a7
	print(a, "(", a2, "x +", a3, ") +", a4, "=", a5, "(", a6, "x +", a7, ") +", a8, )
	# add a subtype with distribtuive property on only one side
	if x == int(input("What is x?")):
		print("yes")
	else:
		print("no, x is", x)

#add inequalities, absolute value, systems of equations

# Generate a quadratic equation

elif task == "quadratic":
	n = 0
	while n <= 0:
		n=int(input("How big do you want your numbers?"))
	a1 = randint(-1*n,n)
	while a1 == 0:
		a1 = randint(-1*n,n)
	a2 = randint(-1*n,n)
	a3 = randint(-1*n,n)
	while a3 == 0:
		a3 = randint(-1*n,n)
	a4 = randint(-1*n,n)
	a = a1*a3
	b = a1*a4+a2*a3
	c = a2*a4
	print(a, "x^2 +", b, "x +", c, "= 0")
	# This needs to be fixed for fractions
	if (float(input("What is x?")) == -1*a2/a1 or -1*a4/a3) and (float(input("What is x?")) == -1*a2/a1 or -1*a4/a3):
		print("yes")
	else:
		print("no, x is", -1*a2/a1, "and", -1*a4/a3)

#add graphing!

