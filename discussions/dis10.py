# EXCEPTIONS, CALCULATOR 10
# Exceptions provide a general mechanism for adding error-handling logic to programs.

# Raising an exception is a technique for interrupting the normal ﬂow of execution in a
# program, signaling that some exceptional circumstance has arisen.

# An exception is an object instance of a class that inherits, either directly or indirectly, from
# the BaseException class

# >>> raise Exception(’An error occurred’)

# 1.1 Questions
try:
	x = 1 / 0
except ZeroDivisionError as e:
	print("handling a", type(e))
	x = 9001

def safe_square(x):
	try:
		return x * x
	except TypeError as e:
		print ('Incorrect argument type')

safe_square('hello')	
safe_square('hello' * 5)
# safe_square('hello' * 'hello')
safe_square(1 * 2.5)
# ######
# safe_square(1/ 0)	

# 2 Calculator

# There are two kinds of expressions.
# A call expression
# A primitive expression

class Pair(object):
    """A pair has two instance attributes: first and second.  For a Pair to be
    a well-formed list, second is either a well-formed list or nil.  Some
    methods only apply to well-formed lists.

    >>> s = Pair(1, Pair(2, nil))
    >>> s
    Pair(1, Pair(2, nil))
    >>> print(s)
    (1 2)
    >>> len(s)
    2
    >>> s[1]
    2
    >>> print(s.map(lambda x: x+4))
    (5 6)
    """
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __repr__(self):
        return "Pair({0}, {1})".format(repr(self.first), repr(self.second))

    def __str__(self):
        s = "(" + str(self.first)
        second = self.second
        # is a instance of pair,convert to str
        while isinstance(second, Pair):
            s += " " + str(second.first)
            second = second.second
        # is a num and not nil print .
        if second is not nil:
            s += " . " + str(second)
        return s + ")"

    def __len__(self):
        n, second = 1, self.second
        while isinstance(second, Pair):
            n += 1
            second = second.second
        if second is not nil:
            raise TypeError("length attempted on improper list")
        return n

    def __getitem__(self, k):
        if k < 0:
            raise IndexError("negative index into list")
        y = self
        for _ in range(k):
            if y.second is nil:
                raise IndexError("list index out of bounds")
            elif not isinstance(y.second, Pair):
                raise TypeError("ill-formed list")
            y = y.second
        return y.first

    def map(self, fn):
        """Return a Scheme list after mapping Python function FN to SELF."""
        mapped = fn(self.first)
        if self.second is nil or isinstance(self.second, Pair):
            return Pair(mapped, self.second.map(fn))
        else:
            raise TypeError("ill-formed list")

    def to_py_list(self):
    	y, result = self, [ ]
    	while y is not nil:
		    result += [y.first]
		    if not isinstance(y.second, Pair) or y.second is not nil:            
		    	raise TypeError("ill-formed list")
		    	y = y.second
    	return result


class nil(object):
    """The empty list"""

    def __repr__(self):
        return "nil"

    def __str__(self):
        return "()"

    def __len__(self):
        return 0

    def __getitem__(self, k):
        if k < 0:
            raise IndexError("negative index into list")
        raise IndexError("list index out of bounds")

    def map(self, fn):
        return self

nil = nil() # Assignment hides the nil class; there is only one instance



# 2.3 Evaluation
t1 =Pair('+', Pair(1, Pair(2, Pair(3, Pair(4, nil)))))
print(t1)
print("shold equal")
print("(+ 1 2 3 4)")

t2 =Pair('+', Pair('1', Pair(Pair('*', Pair(2, Pair(3, nil))), nil)))
print(t2)
print("shold equal")
print("(+ 1 (* (2 3)))")


print("(+ 1 2 (- 3 4))")
print("shold equal")
print(Pair('+',Pair(1,Pair(2,Pair(Pair('-',Pair(3,Pair(4,nil))) ,nil)))))  

# 2.3 Evaluation

# Primitive expressions are evaluated directly. Call expressions are evaluated recursively:
# (1) Evaluate each operand expression, (2) Collect their values as a list of arguments, and
# (3) Apply the named operator to the argument list.
def calc_eval(exp):
	if not isinstance(exp, Pair): #expression is primitive
		return exp
	elif exp.first == 'and':
		return eval_and(exp.second)		
	else:
		operator, operands = exp.first, exp.second
		args = operands.map(calc_eval).to_py_list()
		# ??
		return calc_apply(operator, args)
		
def eval_and(operands):
	cur = operands
	while cur is not nil:
		if not calc_eval(cur.first):
			return False
		cur = cur.second
	return True
# 2.4 Questions

# How many calls to calc eval would they each generate?
# How many calls to calc apply?
# > (+ 2 4 6 8)
5
1
# > (+ 2 (* 4 (- 6 8)))
7
3
# 2. The - operator will fail if given no arguments.
#  Add error handling to raise an exception when this situation is encountered 
#  (the type of exception is unimportant).

def has_zero_division(args):
	if 0 in args[1:]:
		return True
	return False

def calc_apply(operator, args):
	if operator == '+':
		return sum(args)
	elif operator == '-':
		if len(args) == 0:
			raise TypeError('need at least one arg')
		elif len(args) == 1:
			return -args[0]
		else:
			return sum(args[0], [-args for args in args[1:]])
	elif operator == '*':
			return reduce(mul, args, 1)
	elif operator == '/':
		if len(args) == 0 or len(args) == 1:
			raise TypeError('2 arguments should be given,you given ',len(args))
		elif has_zero_division(args):
			raise ZeroDivisionError("devison is 0")
		else:
			return reduce(truediv, args[1:], args[0])
	elif operator == 'and':

			

# 3. We also want to be able to perform division, as in (/ 4 2).
# Supplement the existing code to handle this.
# If division by 0 is attempted, or if there are less than 2 arguments
# supplied, you should raise an exception (the type of exception is unimportant)

# 4. Alyssa P. Hacker and Ben Bitdiddle are also tasked with implementing the and operator, as in (and (= 1 2) (< 3 4)). Ben says this is easy: they just have to follow
# the same process as in implementing * and /. Alyssa is not so sure. Who’s right?


# 5. Now that you’ve had a chance to think about it, you decide to try implementing and
# yourself. You may assume the conditional operators (e.g. <, >, =, etc) have already
# been implemented for you.
