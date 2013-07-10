# Exercise 1
# q1
def square(x):
	return x * x

def net(f,x):
	return -f(x)

def first(x):
		x += 8
		def second(y):
			print('second')
			return x + y
		print('first')
		return second

#Q4 65		
#Q5 13
#Q6 True
#Q7 False
def Troy():
	abed = 0
	while abed < 10:
		britta = lambda: abed
		abed += 1
	abed = 20
	return britta
jeff = Troy()
shirley = lambda : jeff
pierce = shirley()
print (pierce)
print (pierce()) #!!!!!!!!!!!!

#Q8  20

#E2
def default_strategy(my_score,opp_score):
	return 5

def	make_default_strategy:
	return default_strategy

def make_weird_strategy(num_rolls):
	def weird_strategy(score, op_score):
	    return max(num_rolls, (score+op_score)//20)
	return weird_strategy
#E3
#Q1 "who"
#Q2
ninth = lambda x: "Fantastic!" if x == 9 else tenth
# Fantastic!
#Q3
#>>> ninth(2)(10)
# Allons-y
#Q4
# Allons-y
#Q5
#True
#Q6
#Geronimo!
#chanllenge
# one_line = lambda x: "Fantastic!" if x == 9 else lambda y:"Allons-y" if y == 10 else lambda z: "Geronimo!" if z == 11 else one_line

def cycle(f1, f2, f3):
    """ Returns a function that is itself a higher order function 
    >>> add1 = lambda x: x+1 
    >>> times2 = lambda x: 2*x 
    >>> add3 = lambda x: x+3 
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """

    " *** YOUR CODE HERE *** "
	base = lambda x:x
	if n == 0:
		return base

	r = base
	while i <= n:
		if i % 3 == 1:
			r = f1(r)
		elif i % 3 == 2:
			r = f2(r)
		elif i % 3 == 0:
			r = f3(r)
		i = i + 1
	return r
def cycle(f1, f2, f3):
     def ret_fn(n):

         def ret(x):      
             i = 0       
             while i < n:               
                 if i % 3 == 0:
                     x = f1(x) 
                 elif i % 3 == 1:
                     x = f2(x)
                 else:        
                     x = f3(x)
                 i += 1
             return x
             
         return ret
     return ret_fn   