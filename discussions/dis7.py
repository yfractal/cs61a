def countdown(n):
	"""
	>>> countdown(3)
	3
	2
	1
	"""
	print (n)
	if n == 1:
		return 
	countdown(n-1)

def countup(n):
	"""
	>>> countup(3)
	1
	2
	3
	"""
	if n == 1:
		print(n)
		return 
	countup(n-1) #count first 
	print(n) #then print

def expt(base, power):
	"""
	>>> expt(3,2)
	9
	>>> expt(2,3)
	8
	"""
	if power == 0:
		return 1
	elif power == 1:
		return base
	return base * expt(base  ,power - 1)

# !!!!!!!!!!!!!!!!!!!!
def map(fn, seq):
	if len(seq) == 1:
		return [fn(seq[0])] #base
	return [fn(seq[0])] #this turn 
			+ map(fn,seq[1:]) #next turn
# !!!!!!!!!!!!!!!!!!!!

def square(x):
	return x * x 
t_se = [1,2,3,4,5]
r = map(square,t_se)
print(r)

def map2(fn,seq):
	if len(seq) == 0:
		return
	seq[0] = fn(seq[0])
	map(fn,seq[1:])

# 5	

def sum_primes_up_to(n):
	if n <= 1:
		return 0
	if is_prime(n):
		return n + sum_primes_up_to(n -1)
	else:
		return sum_primes_up_to(n-1)

def sum_filter_up_to(n, pred):
	if n <= 0:
		return 0
	if pred(n):
		return n + sum_filter_up_to(n -1,pred)
	else:
		return sum_filter_up_to(n - 1,pred)

# 2 Tree Recursion
# 2.1 Exercises
def count_stair_ways(n):
	"""
	>>> count_stair_ways(1)
	1
	>>> count_stair_ways(2)
	2
	>>> count_stair_ways(3)
	3
	>>> count_stair_ways(4)
	5
	>>> count_stair_ways(6)
	13
	>>> 
	"""
	if n < 0:
		return 0
	elif n == 0:
		return 1
	return count_stair_ways(n-1) + count_stair_ways(n-2)

# 2. Pascal’s triangle
def pascal(row, column):
	"""
	>>> pascal(2,1)
	2
	>>> pascal(5,2)
	10
	"""
	if column == 0:
		return 1
	elif row == column:
		return 1
	elif row < column:
		return 0
	return pascal(row-1,column -1) + pascal(row-1,column)

def hasSum(sum, n1, n2):
	"""
	>>> hasSum(1, 3, 5)
	False
	>>> hasSum(5, 3, 5) # 1(5) + 0(3) = 5
	True
	>>> hasSum(11, 3, 5) # 2(3) + 1(5) = 11
	True
	"""
	if sum < 0:
		return False
	elif sum == 0:
		return True
	return hasSum(sum -n1,n1,n2) or hasSum(sum - n2,n1,n2)

def subset_sum(seq, sum):
	"""
	>>> subset_sum([2, 4, 7, 3], 5) # 2 + 3 = 5
	True
	>>> subset_sum([1, 9, 5, 7, 3], 2)
	False
	>>> subset_sum([1, 1, 5, -1], 3)
	False

	"""	
	if len(seq) == 0 and sum != 0:
		return False
	elif sum < 0:
		return False
	elif sum == 0:
		return True
	return subset_sum(seq[1:], sum - seq[0] ) or subset_sum(seq[1:] , sum )

def mergesort(seq):
	if len(seq) <= 1:
		return seq
	half = len(seq)
	return merge( mergesort(seq[:half]) ,mergesort(seq[half:]) )

def merge(s1,s2):
	"""
	# s1,s2 are in order
	>>> s1 = [2,11,13,15,17]
	>>> s2 = [1,6,7,12,13,14]
	>>> merge(s1,s2)
	[1, 2, 6, 7, 11, 12, 13, 13, 14, 15, 17]
	"""
	if len(s1) == 0:
		return s2
	elif len(s2) == 0:
		return s1
	elif s1[0] < s2[0]:
		return [s1[0]] + merge(s1[1:], s2)
	else:
		return [s2[0]] + merge(s1, s2[1:])


# 3 Iteration vs. Recursion
def factorial_recursive(n):
	if n <= 0:
		return 1
	else:
		return n * factorial_recursive(n-1)

def factorial_iterative(n):
	total = 1
	while n > 0:
		total = total * n
		n = n - 1
	return total

def fib_r(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return fib_r(n - 1) + fib_r(n - 2)

def fib_i(n):
	curr, next = 0, 1
	while n > 1:
		curr, next = next, curr + next
		n = n - 1
	return curr
# Iteratively, you
# need to keep track of more numbers and have a better understanding of what the code is
# doing