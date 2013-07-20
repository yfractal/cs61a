# tuples
def foo(a,b):
	return a,b

tup = foo(1,2)	
# >>> tup
# (1,2)

# >>> a = (1, 2, 3)
# >>> b = (4, 5, 6)
# >>> c = a + b
# >>> c

def sum(tup):
	""" Sums up the tuple.
	>>> sum((1, 2, 3, 4, 5))
	15
	"""
	r = 0
	for e in tup:
		r += e
	return r

def min_element(tup):
	""" Returns the minimum element in tup.
	>>> a = (1, 2, 3, 2, 1)
	>>> min_element(a)
	1
	"""
	r_min = tup[0]
	for e in tup:
		r_min = min(r_min,e)
	return r_min

def map_tuple(func, tup):
	"""Applies func to each element of tup and returns a new tuple.
	>>> a = (1, 2, 3, 4)
	>>> func = lambda x: x * x
	>>> map_tuple(func, a)
	(1, 4, 9, 16)
	"""
	r = ()
	for e in tup:
		r += (func(e),)
	return r

def cartesian_product(tup_1, tup_2):
	"""Returns a tuple that is the cartesian product of tup_1 and tup_2.
	>>> X = (1, 2)
	>>> Y = (4, 5)
	>>> cartesian_product(X, Y)
	((1, 4), (4, 1), (1, 5), (5, 1), (2, 4), (4, 2), (2, 5), (5, 2))

	"""	

	r = ()
	for e1 in tup_1:
		for e2 in tup_2:
			r += ((e1,e2),(e2,e1))
	return r

def cartesian_product(tup_1, tup_2):
	product = ()
	for elem1 in tup_1:
		for elem2 in tup_2:
			product += ((elem1, elem2), )
			product += ((elem2, elem1), )
	return product	

# 3 Sequence Iteration with For Loops
def sum_sequence(sequence):
	r = 0
	for e in sequence:
		r += e
	return r

def filter(pred, sequence):
	"""
	>>> filter(lambda x: x % 2 == 0, (1, 4, 2, 3, 6))
	(4, 2, 6)
	"""
	r = ()
	for e in sequence:
		if pred(e):
			r += (e,)
	return r


# 4 Newton’s Method
def approx_deriv(fn, x, dx=0.00001):
	return (fn(x+dx)-fn(x))/dx

def newtons_method(fn, guess=1, max_iterations=100):
	ALLOWED_ERROR_MARGIN = 0.0000001
	i = 1
	while abs(fn(guess)) > ALLOWED_ERROR_MARGIN and i <= max_iterations:
		guess = guess - fn(guess) / approx_deriv(fn, guess)
		i += 1
	return guess

def cube_root(x):
	f = lambda r: r * r * r - x		
	return newtons_method(f, 0)




def newtons_method2(fn, guess=1, max_iterations=100):
	def newtons_update(guess, min_size=0.001):
		d = derivative(fn,guess)
		if d < 0.001:
			return None
		return guess - fn(guess) / d

	def newtons_done(guess):
		if guess == None:
			return True
		ALLOWED_ERROR_MARGIN= 0.0000001
		return abs(fn(guess)) <= ALLOWED_ERROR_MARGIN

	return iter_improve(newtons_update, newtons_done, guess,max_iterations)



def iter_improve(update, isdone, guess=1, max_iterations=100):
	i = 1
	while not isdone(guess) and i <= max_iterations:
		guess = update(guess)
		i += 1
	return guess	


# 6 Data Abstraction
def make_person(first, last, age):
	return (first, last, age)

def get_first(person):
	return person[0]

def get_last(person):
	return person[1]

def get_age(person):
	return person[2]	

# 2
def make_point(x, y):
	return (x, y)

def get_x(point):
	return point[0]

def get_y(point):
	return point[1]

def make_seg(pt1, pt2):
	return (pt1, pt2)

def start_pt(seg):
	return seg[0]

def end_pt(seg):
	return seg[1]



def reflect_y(p):
	x = get_x(p)
	y = get_y(p)
	return make_point(-x,y)

def reflect_across_y(seg):
	"""Returns a line segment that is the y-axis reflection of seg.
	>>> pt1 = make_point(0, 0)
	>>> pt2 = make_point(4, 5)
	>>> line_seg = make_seg(pt1, pt2)
	>>> reflect_across_y(line_seg)
	((0, 0), (-4, 5))
	"""
	s_p = start_pt(seg)
	e_p = end_pt(seg)	
	return make_seg(reflect_y(s_p),reflect_y(e_p))

def midpoint(seg):
	first_pt = start_pt(seg)
	sec_pt = end_pt(seg)
	new_x = (get_x(first_pt) + get_x(sec_pt)) // 2
	new_y = (get_y(first_pt) + get_y(sec_pt)) // 2
	return make_point(new_x,new_y)
