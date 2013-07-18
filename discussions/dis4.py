# MUTABLE LISTS AND DICTIONARIES
# 1
# append(element),extent(seq),remove(element),\
# pop(i) removes the element at index i and returns that removed element
"""
>>> bob = [4,2,3,1]
>>> sorted(bob)
[1, 2, 3, 4]
>>> bob
[4, 2, 3, 1]

>>> bob.sort()
>>> bob
[1, 2, 3, 4]
"""

# 1.2 Writing list functions
"""
 should mutate the original list
 should NOT create any new lists
 should NOT return anything
"""

# 1
def map_mut(fn, lst):
	"""Maps fn onto lst by mutation.
	>>> lst = [1, 2, 3, 4]
	>>> map_mut(lambda x: x**2, lst)
	>>> lst
	[1, 4, 9, 16]
	"""
	i = 0
	while i < len(lst):
		lst[i] = fn(lst[i])
		i += 1

# 2
def shift_left(lst, n):
	"""Shifts the elements of lst over by n indices.
	>>> lst = [1, 2, 3, 4, 5]
	>>> shift_left(lst, 2)
	>>> lst
	[3, 4, 5, 1, 2]
	"""

	# shift n times
	i_n = 0
	while i_n < n:
		# shift one 
		tmp = lst[0]
		i = 0
		while i < len(lst) - 1:
			lst[i] = lst[i+1]
			i += 1
		lst[-1]	= tmp

		i_n += 1


# 3
def filter_mut(pred, lst):
	"""Filters lst by mutating it.
	>>> lst = [1, 2, 3, 4]
	>>> is_even = lambda x: x % 2 == 0
	>>> filter_mut(is_even, lst)
	>>> lst
	[2, 4]
	"""
	# pop when pred is true
	i = 0
	while i < len(lst):
		if not pred( lst[i] ):
			lst.pop(i)
		else:
			i += 1

# 1.3 Slicing
#  lst[start:end:incr] where start, end, and incr are integers
"""
>>> a = [0, 1, 2, 3, 4, 5, 6]
>>> a[1:6:2]
[1, 3, 5]
>>> a[1:4:] # equivalent to a[1:4:1] or a[1:4]
[1, 2, 3]
NOTE: slicing does NOT mutate the original list – it creates a new list.
"""

# 1.4 Questions
"""
>>> a= [3,1,4,2,5,3]
>>> a[:4]
[3, 1, 4, 2]
>>> a[1::2]
[1, 2, 3]
>>> a[:]
[3, 1, 4, 2, 5, 3]
>>> a[4:2]
[]
>>> a[1:-2]
[1, 4, 2]
>>> a[::-1]
[3, 5, 2, 4, 1, 3]
"""
# 1.5 List comprehensions
"""
[ <map expr> for <name> in <sequence> if <filter expr> ]
"""
def foo(lst):
	new = []
	for elem in lst:
		if elem % 2 == 0:
			new += [elem**2]
	return new

def foo(lst):
	return [ elem**2 for elem in lst if elem %2 == 0 ]


# 1.6 Questions

"""
>>> seq = range(5)
>>> x = [x * x for x in seq]
>>> x
[0, 1, 4, 9, 16]
>>> [elem + 1 for elem in (1,2,3,4) if elem % 2 == 0]
[3, 5]
>>> [x + y for x in (1,4) for y in [5,2] ]
[6, 3, 9, 6]
>>> [[x + y for x in (1,4)] for y in [5,2]]
????????????????????????????
????[[6, 9], [3, 6]]????????
????????????????????????????
"""

# 2 Dictionaries
"""
 not ordered: the order in which you enter key/value may not be the order in which
they are stored in the dictionary.
 mutable: you can add and remove keys from dictionaries
 one-to-one: a key can only map to one value (although that value can be a tuple of
elements)

>>> del names[’john’] # delete a key/value pair
>>> names
"""

# 2.1 Questions
def make_inverse_dict(d):
	r = {}
	for k,v in d.items():
		r[v] = k
	return r






