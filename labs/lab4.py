def make_rat(num, den):
  return (num, den)

def num(rat):
  return rat[0]

def den(rat):
  return rat[1]

def mul_rat(a, b):
  new_num = num(a) * num(b)
  new_den = den(a) * den(b)
  return make_rat(new_num, new_den)

def div_rat(a,b):
	new_num = num(a) * den(b)
	new_den = den(a) * num(b)
	return make_rat(new_num, new_den)

def str_rat(x):
  #from lecture notes
  """Return a string 'n/d' for numerator n and denominator d."""
  return '{0}/{1}'.format(num(x), den(x))


#Ex 5
#x,y
#c 
def make_point(x,y):
	return (x,y)
#s
def x_coord(p):
	return p[0]
def y_coord(p):
	return p[1]


def dist(s,e):
	dx = x_coord(e)	- x_coord(s)
	dy = y_coord(e)	- y_coord(s)
	return square_root( square(dx) + square(dy) )
#segment
#c 

def make_segment(start_p,end_p):
	return (start_p,end_p)
#s

def start_segment(segment):
	return segment[0]

def end_segment(segment):
	return segment[1]

def mid_point(segment):
	s = start_segment(segment)
	e = end_segment(segment)
	new_x = (x_coord(s) + x_coord(e)) / 2
	new_y = (y_coord(s) + y_coord(e)) / 2
	return make_point(new_x,new_y)

def square(x):
	return x * x

def square_root(x):
	assert x >= 0 ,"give me a possible number please"
	return x ** 0.5


#Ex 6

def make_pair(x, y):
       """Return a function that behaves like a pair."""
       def dispatch(m):
       	   assert m <= 2,"Message not recognized"
           if m == 0:
               return x
           elif m == 1:
               return y
       return dispatch


#Ex 7

def make_rectangle(p1,p2,p3):
	return (p1,p2,p3)

def first_point(rectangle):
	return rectangle(0)

def second_point(rectangle):
	return rectangle(1)

def third_point(rectangle):
	return rectangle(2)

def perimeter(rectangle):
	p1 = first_point(rectangle)
	p2 = second_point(rectangle)
	p3 = third_point(rectangle)

	d1 = dist(p1,p2)
	d2 = dist(p2,p3)
	e3 = dist(p3,p1)

	return d1 + d2 + d3

def area(rectangle):
	# S=√[p(p-a)(p-b)(p-c)] [p=1/2(a+b+c)]（海伦--秦九韶公式）
	p1 = first_point(rectangle)
	p2 = second_point(rectangle)
	p3 = third_point(rectangle)

	d_a = dist(p1,p2)
	d_b = dist(p2,p3)
	e_c = dist(p3,p1)

	p = d_a + d_b + d_c
	return square_root(p * (p - d_a) * (p - d_b) * p_c )
