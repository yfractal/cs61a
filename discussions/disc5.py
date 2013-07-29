# MORE MUTATION, NONLOCAL, AND MORE ENVIRONEMENTS
# 1 More Mutation (is vs. ==)
""" 
>>> x = [1, 2, 3]
>>> y = [1, 2, 3]
>>> z = x
>>> x == y
True
>>> x is y
False
>>> z is x
True
>>> x is z
True
"""

# 1.1 What would Python print?
"""
>>> ls = [1,2,3,4]
>>> list = [1,2,3,4]
>>> ls == list
True
>>> ls is list
False
>>> x = [100,101]
>>> ls[2] = x
>>> list[3] = ls[2]
>>> list[3] is x
True

>>> ls
[1, 2, [100, 101], 4]
>>> x = ls
>>> ls[0] = x
>>> ls is ls[0] 
# intistring...
True

>>> ls == ls[0]
True

>>> 
"""
# 2 Nonlocal Assignment (Modeling State)
"""
Referentially Transparent -- an expression is referentially transparent if it can be replaced with its 
value, without any change in program behavior.
For instance, the expression
add(sum((1, 2, 3)), square(4))
is exactly equivalent to replacing sum((1, 2, 3)) with its value, 6:
add(6, square(4))
"""
def make_delayed_repeated():
	my_phrase = "..."
	def repeater(in_):
		to_return = my_phrase
		my_phrase = in_ 
		return to_return
	return repeater

def make_delayed_repeater():
	my_phrase = '...'
	def repeater(in_):
		nonlocal my_phrase
		to_return = my_phrase
		my_phrase = in_
		return to_return
	return repeater	

"""
that nonlocal will stop before the global frame, in other words it will not find 
variables in the global frame.
The variable can't already exist in the current scope
"""


# 2.1 What would Python print? 
name = 'rose'
def my_func():
	name = 'martha'
	return None
my_func()
print(name)

# b.) 
name = 'ash'
def abra(age):
	def kadabra(name):
		def alakazam(level):
			nonlocal name
			name = 'misty'
			return name
		return alakazam
	return kadabra
print(abra(12)('sleepy')(15))

# c.)
def f(t=0):
	def g(t=0):
		def h():
			nonlocal t
			t = t + 1
		return h, lambda: t 
		# t is nonlocal 
	h, gt = g()
	return h, gt, lambda: t
	# t in g
h, gt, ft = f()
print(ft(), gt())
print(h())
"0 0\n None"
print(h())
print(ft(), gt())
"None\n0 2"

# 2.2 More Environments!!
def boring(x):
	def why(y):
		x = y
	why(5)
	return x
print(boring(10))

def interesting(x):
	def because(y):
		nonlocal x
		x = y
	because(5)
	return x
print(interesting(3))

def make_person(name):
	def dispatch(msg):
		if msg == 'name':
			return name
		elif msg == 'aki-ify':
			nonlocal name
			name = 'aki'
		else:
			print("wat")
	return dispatch

stephen = make_person('stephen')
print(stephen('aki-ify'))
print(stephen('name'))

# 3 Functions with Local State 
"""
This is a precursor to a programming paradigm called Object-Oriented Programming (OOP), a popular 
style of programming that's aimed at making programs easier to reason about.
"""

# 3.1 Nonlocal State Function with an Environment 


def make_counter(x):
	init_val = x
	def dispatch(m):
		nonlocal x
		if m == ‘inc’:
			x += 1
		elif m == ‘count’:
			return x
		elif m == ‘reset’:
			x = init_val
 	return dispatch
