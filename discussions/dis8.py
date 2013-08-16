# 1 Recursive Lists
# 1.1 Questions
def len_rlist(s):
	if s == None:
		return 0
	return 1 + len_rlist( s.rest)

def getitem_rlist(s, index):
	if s == None:
		return None
	if index == 0:
		return s.first
	return getitem_rlist(s.rest,index-1)

# 3.
def insert_rlist(s, index, value):
	"""
	>>> s = Rlist(2, Rlist(4, Rlist(5)))
	>>> insert_rlist(s, 1, 3)
	>>> s
	Rlist(2, Rlist(3, Rlist(4, Rlist(5))))
	"""
# 	if index == 0:
# # !!!!!!!!!!!!!!		
# 		s.rest = Rlist(s.first, s.rest)
# 		s.first = value		
# # !!!!!!!!!!!!!!		
# 	return Rlist(s.first,insert_rlist(s.rest, index-1,value))

	if index == 0:
		s.rest = Rlist(s.first, s.rest)
		s.first = value
	else:
		while index > 1:
			if s.rest == Rlist.empty:
				return "Index out of bounds"
		s, index = s.rest, index-1
		s.rest = Rlist(value, s.rest)

# 2 Trees
# 2.1 Our Implementation
# 2.2 Questions
def square_tree(t):
	""" Mutates a Tree t by squaring all its elements """
	if t == None:
		return None
	return Tree(t.entry * t.entry,square_tree(t.left),square_tree(t.right))

def square_tree2(t):
	if t is None:
		return
	t.entry = square(t.entry)
	square_tree2(t.left)
	square_tree2(t.right)	

def height(t):
	"""Returns the height of the Tree t."""
	if t is None:
		return 0
	return 1 + max( height(t.left) , height(t.right) )

def tree_size(t):
	"""Returns the number of items in a Tree t."""	
	if t is None:
		return 0
	if t.is_leaf:
		return 1		
	return 1 + tree_size(t.left)  + tree_size(t.right)
	
def find_path(t, entry):
# 	if t.is_leaf():
# 		if t.entry == entry:
# 			return true
# 		else:
# 			return false
# # !!!!!!!!!!!!			# 
# 	flag = find_path(t.left,entry) or find_path(t.right,entry)
# 	if flag:
# 		return entry
# # !!!!!!!!!!!!!!!
	if t is None or (t.is_leaf and t.entry != entry):
		return False
	elif t.entry == entry:
		return (entry,)
	else:
		left_path = find_path(t.left, entry)
		if left_path:
# !!!!!!!!!!!!			# 
			return (t.entry,) + left_path
		right_path = find_path(t.right, entry)
		if right_path:
			return (t.entry,) + right_path
		return False
# !!!!!!!!!!!!			# 


	# flag  =  false
	# if t.entry == entry:
	# 	return the tuple
	# if t == None:
	# 	return False

	# def find_path_h(t,entry):
	# 	if t.entry == entry:
	# 		return True
	# 	if t == None:
	# 		return False
	# 	t.flag = find_path_h(t.left,entry) or find_path_h(t.right,entry)


	# s = []
	# def travel(t):
	# 	if t.flag == true:
	# 		s.append(t.entry)
	# 	travel(t.left)
	# 	travel(t.right)

	# find_path_h(t,entry)
	# travel(t)
	# return tuple(s)
# left find(t,entry):
# 	if t.entry == entry:
# 		return True
# 	if t == None:
# 		return False
# 	return (entry ,find(t.left,entry) )or find(t.right,entry)

class Rlist(object):
    """A recursive list consisting of a first element and the rest."""

    class EmptyList(object):
        def __len__(self):
            return 0

    empty = EmptyList()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __repr__(self):
        args = repr(self.first)
        if self.rest is not Rlist.empty:
            args += ', {0}'.format(repr(self.rest))
        return 'Rlist({0})'.format(args)

    def __len__(self):
        return 1 + len(self.rest)

    def __getitem__(self, i):
        if i == 0:
            return self.first
        return self.rest[i-1]

