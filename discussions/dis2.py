def is_prim(n):
	k = 2
	while k * k <= n:
		if n % k == 0:
			return False
		k += 1
	return true


def nth_prime(n):
	count,curr = 1,2
	p = 2	
	while count < n:
		curr += 1
		if is_prim(curr):
			count += 1
	return curr


def print_nth_prime(n):
	i = 0
	while i < n:
		print(nth_prime(i))
		i += 1


def nth_fib(n):
	if n == 1 or n == 2:
		return 1
	else:
		return nth_fib(n - 1) + nth_fib(n-2)


def nth_fib2(n):
	if n <= 2:
		return 1
	fib1 , fib2 ,i =1,1,0		
	while curr < n:
		fib2,fib1 = fib1 + fib2, fib2
		n += 1
	return fib2		

def nth_fib3(n):
	count, curr, next = 1, 0, 1
	while count < n:
		curr, next = next, curr + next
		count += 1
	return curr	


# from math import sqrt
def square(n):
	return n * n


def square_every_number(n):
	every(square,n)	

def every(f,n):
	i = 1
	while i <= n:
		print(f(n))

def double(n):
	return 2 * n

def double_every_number(n):
	every(double,n)


def keep(cond, n):
	i = 1
	while i <= n:
		if cond(i):
			print (i)
		i += 1

def and_add_one(f):
	return f(x) + 1

def and_add(f,n):
	return f(x) + n



def skipped(f):
	def g():
		return f
	return g

def composed(f, g):
	def h(x):
 		return f(g(x))
	return h


def added(f, g):
	def h(x):
		return f(x) + g(x)
	return h

def square(x):
	return x*x

def two(x):
	return 2


















