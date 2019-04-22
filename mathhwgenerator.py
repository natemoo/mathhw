from random import uniform, randint
from functions import *
from math import floor

# Prompt the user for a task
# Tasks currently supported:
# Arithmetic with whole numbers, integers, fractions, and decimals
# onestep (one step equations)
# twostep (two step equations)
# distprop (distributive property equations)
# simpbothsides (simple equations with variables on both sides)
# distbothsides (equations using the distributive property with variables on both sides)
# quadratic (quadratic equation with real solutions; broken for fractions)

while True:

	task = input("What do you want to do?")

	# Section: Arithmetic
	# Whole number arithmetic
	if task == "add":
		arithmetic()

	elif task == "subtract":
		arithmetic("subtraction")

	elif task == "multiply":
		arithmetic("multiplication")

	elif task == "divide":
		arithmetic("division")

	# Integer Arithmetic
	elif task == "addneg":
		arithmetic(neg=True)

	elif task == "subtractneg":
		arithmetic("subtraction",True)

	elif task == "multiplyneg":
		arithmetic("multiplication",True)

	elif task == "divideneg":
		arithmetic("division",True)

	# Fraction arithmetic
	elif task == "addfract":
		prompt()
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
		prompt()
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
		prompt()
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
		prompt()
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
		arithmetic(dec=True)

	elif task == "subtractdec":
		arithmetic("subtraction",False,True)

	elif task == "multiplydec":
		arithmetic("multiplication",False,True)

	elif task == "dividedec":
	#This does not quite work...
		arithmetic("division",False,True)

	# Section: Algebra

	# These tasks all have simple solutions (integers for linear equations and real numbers for quadratics)

	# Generate a onestep equation

	elif task == "onestep":
		n = prompt()
		co = coeffs(1,n)
		c = constants(1,n,True)
		s = randint(1,4)
		if s == 1:
			b = co[0]*c[0]
			print(co[0], "x =", b)
		elif s == 2:
			b = c[0]/co[0]
			print("x/", co[0], "=", b)
		elif s == 3:
			b = c[0] + co[0]
			print("x +", co[0], "=", b)
		elif s == 4:
			b = c[0] - co[0]
			print("x -", co[0], "=", b)
		question(x=c[0])

	# Generate a two step equation

	elif task == "twostep":
		n = prompt()
		c = constants(2,n,True)
		co = coeffs(1,n)
		s = randint(1,2)
		if s == 1:
			b = co[0]*c[0]+c[1]
			print(co[0], "x +", c[1], "=", b)
		elif s == 2:
			b = co[0]*c[0]-c[1]
			print(co[0],"x -", c[1], "=", b)
		question(x=c[0])

	# Generate a distributive property equation

	elif task == "distprop":
		n = prompt()
		co = coeffs(2,n)
		c = constants(3,n,True)
		s = randint(1,2)
		if s == 1:
			b = c[1] + co[0]*co[1]*c[0]+co[0]*c[2]
			print(c[1], "+", co[0], "(", co[1], "x +", c[2], ") =", b)
		elif s == 2:
			b = c[1]*x + co[0]*co[1]*c[0]+co[0]*c[2]
			print(c[1], "x +", co[0], "(", co[1], "x +", c[2], ") =", b)
		question(x=c[0])

	# Generate an equation with variables on both sides in the form ax + b = cx + d

	elif task == "simpbothsides":
		n = prompt()
		co = coeffs(2,n)
		c = constants(2,n,True)
	#	s = randint(1,4)
	#	if s == 1:
		b = co[0]*c[0]+c[1]-co[1]*c[0]
		print(co[0], "x +", c[1], "=", co[1], "x +", b)
	#	if s == 2:
	#		b = c[0]/co[0]+c[1]-co[1]*c[0]
	#		print("x/", co[0], "+", c[1], "=", co[1], "x +", b)
	#	if s == 3:
	#		b = c[0]/co[0]+c[1]-c[0]/co[1]
	#		print("x/", co[0], "+", c[1], "=", "x/", co[1], "+", b)
	#	if s == 4:
	#		b = c[0]/co[0]-co[1]*c[0]
	#		print("x/", co[0], "=", co[1], "x +", b)
		question(x=c[0])

	# Generate an equation with variables on both sides using the distributive property

	elif task == "distbothsides":
		n = prompt()
		co = coeffs(4,n)
		c = constants(4,n,True)	
		while co[3] == -1*co[0]*co[1]/co[2]:
			co.insert(3, randint(-1*n,n))
		b = co[0]*co[1]*c[0]+co[0]*c[1]+c[2]-co[2]*co[3]*c[0]-co[2]*c[3]
		print(co[0], "(", co[1], "x +", c[1], ") +", c[2], "=", co[2], "(", co[3], "x +", c[3], ") +", b, )
		# add a subtype with distribtuive property on only one side
		question(x=c[0])

	#add inequalities, absolute value

	# Systems of Equations

	elif task == "2x2system1":
		n = prompt()
		co = coeffs(4,n)
		c = constants(2,n)
		c.append(co[0]*c[0]+co[1]*c[1])
		c.append(co[2]*c[0]+co[3]*c[1])
		print(f"{co[0]}x + {co[1]} y = {c[2]} \n{co[2]}x + {co[3]} y = {c[3]}")
		question(x=c[0],y=c[1])

	elif task == "2x2system2":
		n = prompt()
		co = coeffs(3,n)
		c = constants(2,n)
		c.append(co[0]*c[0]+co[1]*c[1])
		c.append(co[0]*c[0]+co[2]*c[1])
		s = randint(0,2)
		if s == 0:
			print(f"{co[0]}x + {co[1]} y = {c[2]} \n{co[0]}x + {co[2]} y = {c[3]}")
			question(x=c[0],y=c[1])
		if s == 1:
			print(f"{co[1]}x + {co[0]} y = {c[2]} \n{co[2]}x + {co[0]} y = {c[3]}")
			question(x=c[1],y=c[0])

	elif task == "2x2system3":
		n = prompt()
		co = coeffs(3,n)
		c = constants(2,n)
		co.append(-1*co[0])
		c.append(co[0]*c[0]+co[1]*c[1])
		c.append(co[3]*c[0]+co[2]*c[1])
		s = randint(0,2)
		if s == 0:
			print(f"{co[0]}x + {co[1]} y = {c[2]} \n{co[3]}x + {co[2]} y = {c[3]}")
			question(x=c[0],y=c[1])
		if s == 1:
			print(f"{co[1]}x + {co[0]} y = {c[2]} \n{co[2]}x + {co[3]} y = {c[3]}")
			question(x=c[1],y=c[0])

	# FOIL

	elif task == "foil":
		n = prompt()
		co = coeffs(4,n)
		print(f"({co[0]}x + {co[1]})({co[2]}x + {co[3]})")
		input("What is the answer?")
		print(f"The answer is {co[0]*co[2]}x^2 + {co[0]*co[3]+co[1]*co[2]}x + {co[1]*co[3]}")

	# Generate a quadratic equation

	elif task == "quadratic":
		n = prompt()
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

	#Generate a rational expression
	elif task == "simprat":
		n = prompt()
		co = coeffs(6,n)
		s = randint(0,2)
		if s == 0:
			print(f"{co[0]*co[2]}x^2 + {co[0]*co[3]+co[1]*co[2]}x + {co[1]*co[3]} / {co[0]*co[4]}x^2 + {co[0]*co[5]+co[1]*co[4]}x + {co[1]*co[5]}")
			input("What is the answer?")
			print(f"The answer is {co[2]}x+{co[3]} / {co[4]}x+{co[5]}")
		if s == 1:
			print(f"({co[0]}x+{co[1]})({co[2]}x+{co[3]}) / ({co[0]}x+{co[1]})({co[4]}x+{co[5]})")
			input("What is the answer?")
			print(f"The answer is {co[2]}x+{co[3]} / {co[4]}x+{co[5]}")
		#add more types?


	# Algebra Word Problems

	# Consecutive Integer WP
	elif task == "consecutiveint":
		n = prompt()
		c = randint(0,n)
		w = randint(2,6)
		total = 0
		for i in range(w):
			total = total + c + i
		print(f"The sum of {w} consecutive integers is {total}.")
		nextw = "first"
		for j in range(w):
			answer = input(f"What is the {nextw} number?")
			if c + j != int(answer):
				print(f"No, the number was {c + j}.")
				break
			nextw = "next"
			print("Yes!")

	# One number is... Word Problems
	# maybe add "less than" capability to this for co[2]?
	elif task == "onenumberis":
		n = prompt()
		co = coeffs(3,n,False)
		co.append(co[0]*co[1]+co[2])
		answer = input(f"One number is {co[2]} more than {co[1]} times another number. Their sum is {co[0]+co[3]}. What is the first number?")
		if int(answer) == co[0]:
			answer = input("Right! What is the second number?")
			if int(answer) == co[3]:
				print("Yup!")
			else:
				print(f"no, the number was {co[3]}.")
		else:
			print(f"no, the number was {co[0]}.")

	#Age WP
	elif task == "agewp":
		age1 = randint(1,30)
		multiplier = randint(2,6)
		age2 = age1*multiplier
		years = randint(-20,20)
		while years == 0 or age1 + years <=0:
				years = randint(-20,20)
		input(f"One person is {multiplier} times as old as another person. In {years} years, the sum of their ages will be {age1 + years + age2 + years}. How old is each now?")
		print(f"They are {age1} and {age2} years old.")


	elif task == "agewp2":
		s = randint(0,3)
		if s == 0:
			difference = 2
			while difference != 0:
				age1 = randint(1,25)
				multiplier = randint(2,6)
				age2 = age1*multiplier
				years = randint(-20,20)
				while years == 0 or age1 + years <=0:
					years = randint(-20,20)
				age1b = age1 + years
				age2b = age2 + years
				multiplier2 = floor(age2b / age1b)
				difference = age2b - (age1b*multiplier2)
			input(f"Betty is {multiplier} times as old as Jonny. In {years} years, Betty will be {difference} more than {multiplier2} times Jonny's age. How old is each now?")
			print(f"They are {age1} and {age2} years old.")
		if s == 1:
			difference = 2
			while difference != 0:
				age1 = randint(1,25)
				diff = randint(2,6)
				age2 = age1 + diff
				years = randint(-20,20)
				while years == 0 or age1 + years <=0:
					years = randint(-20,20)
				age1b = age1 + years
				age2b = age2 + years
				multiplier2 = floor(age2b / age1b)
				difference = age2b - (age1b*multiplier2)
			input(f"Betty is {diff} years older than Jonny. In {years} years, Betty will be {difference} more than {multiplier2} times Jonny's age. How old is each now?")
			print(f"They are {age1} and {age2} years old.")
		if s == 2:
			multiplier2 = 2
			while multiplier2 != 1:
				age1 = randint(1,25)
				multiplier = randint(2,6)
				age2 = age1*multiplier
				years = randint(-20,20)
				while years == 0 or age1 + years <=0:
					years = randint(-20,20)
				age1b = age1 + years
				age2b = age2 + years
				multiplier2 = floor(age2b / age1b)
				difference = age2b - (age1b*multiplier2)
			input(f"Betty is {multiplier} times as old as Jonny. In {years} years, Betty will be {difference} more than {multiplier2} times Jonny's age. How old is each now?")
			print(f"They are {age1} and {age2} years old.")

	elif task == "agewp3":
		s = randint(0,2)
		if s == 0:
			age1 = randint(1,25)
			multiplier = randint(2,6)
			age2 = age1*multiplier
			years = randint(-20,20)
			while years == 0 or age1 + years <=0:
				years = randint(-20,20)
			age1b = age1 + years
			age2b = age2 + years
			multiplier2 = floor(age2b / age1b)
			difference = age2b - (age1b*multiplier2)
			input(f"Betty is {multiplier} times as old as Jonny. In {years} years, Betty will be {difference} more than {multiplier2} times Jonny's age. How old is each now?")
			print(f"They are {age1} and {age2} years old.")
		if s == 1:
			age1 = randint(1,25)
			diff = randint(2,6)
			age2 = age1 + diff
			years = randint(-20,20)
			while years == 0 or age1 + years <=0:
				years = randint(-20,20)
			age1b = age1 + years
			age2b = age2 + years
			multiplier2 = floor(age2b / age1b)
			difference = age2b - (age1b*multiplier2)
			input(f"Betty is {diff} years older than Jonny. In {years} years, Betty will be {difference} more than {multiplier2} times Jonny's age. How old is each now?")
			print(f"They are {age1} and {age2} years old.")

	elif task == "agewp4":
		age1 = randint(1,25)
		multiplier = randint(2,6)
		age2 = age1*multiplier
		years = randint(-20,20)
		while years == 0 or age1 + years <=0:
			years = randint(-20,20)
		input(f"One person is {age1} years old and another person is {age2} years old. In how many years will the sum of their ages be {age1 + years + age2 + years}?")

	elif task == "agewp5":
		age1 = randint(1,25)
		multiplier = randint(2,6)
		age2 = age1*multiplier
		years = randint(-20,20)
		while years == 0 or age1 + years <=0:
			years = randint(-20,20)
		age1b = age1 + years
		age2b = age2 + years
		multiplier2 = floor(age2b / age1b)
		difference = age2b - (age1b*multiplier2)
		input(f"One person is {age1} years old and another person is {age2} years old. In how many years will they be {difference} more than {multiplier2} times the other person's age?")

	elif task == "motionwp1":
		r1 = randint(1,100)
		t1 = randint(1,12)
		d1 = r1*t1
		r2 = randint(1,100)
		t2 = t1
		d2 = r2*t2
		dt = d1 + d2
		input(f"Nate and Joseph are traveling in opposite directions. Nate is going {r1} mph and Joseph is going {r2} mph. After how long will they be {dt} miles apart?")
		print(f"After {t1} hours")

	elif task == "motionwp2":
		r1 = randint(1,100)
		t1 = randint(1,12)
		d1 = r1*t1
		r2 = randint(1,100)
		t2 = t1
		d2 = r2*t2
		dt = d1 + d2
		input(f"Nate and Joseph are {dt} miles apart. They want to meet, so they each leave their location at the same time. Nate is going {r1} mph and Joseph is going {r2} mph. After how long will they meet?")
		print(f"After {t1} hours")

	elif task == "motionwp3":
		r1 = 5*randint(1,20)
		r2 = 5*randint(2,25)
		while r2 <= r1:
			r2 = 5*randint(2,25)
		lcm = r2
		while (lcm % r1 != 0) or (lcm % r2 != 0):
			lcm += 1
		d = randint(1,4)*lcm
		t1 = d/r1
		t2 = d/r2
		ti = t1-t2
		input(f"Nate and Joseph are racing to South America on hang gliders after school one day. Nate leaves first, traveling at {r1} mph. Joseph leaves {ti} hours later, traveling at {r2} mph. How many hours after Joseph leaves will he catch up to Nate?")
		print(f"After {t2} hours.")

	elif task == "test":
		binomial1 = binomial()
		binomial2 = binomial()
		binomial1.expression()
		binomial2.expression()
		trinomial1 = trinomial(binomial1, binomial2)
		trinomial1.expression()





