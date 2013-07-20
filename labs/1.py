from math import sqrt, pow

def sum(a,b):
	return a + b
def square(x):
	return x * x

def sum_of_squares(a, b):	
	return sum(square(a),square(b))

def distance(x1, y1, x2, y2):	
	dx = x2 - x1
	dy = y2 - y1
	return sqrt(sum_of_squares(dx,dy))

def biggest_of_three(a, b, c):	
	return max(max(a,b),c)