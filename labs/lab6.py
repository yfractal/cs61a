# Nonlocal
# 8
# 12
# 9
# 12

def make_funny_adder(n):
        def adder(x):
            if x == 'new':
                nonlocal n
                n = n + 1
            else:
                return x + n
        return adder

def make_fib():
	n = 0
	n_minus_2 = 1
	n_minus_1 = 1

	def next_fib():
		nonlocal n,n_minus_1,n_minus_2

		if n < 2:
			n +=1
			return 1
		n_minus_1 ,n_minus_2 = n_minus_1 + n_minus_2,n_minus_1
		n += 1
		return n_minus_1

	return next_fib

def make_fib2():
          n = 0
          first, second = 1, 1
          def fib():
              nonlocal n, first, second
              if n == 0:
                  n += 1
                  return first
              elif n == 1:
                  n += 1
                  return second
              else:
                  first, second = second, first + second
                  return second
          return fib

# Shakespeare and Dictionaries

"""
Code for CS61A lab 6, Fall 2012. 
"""

def build_successors_table(tokens):
    """Return a dictionary: keys are words; values are lists of successors.
    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']

    >>> table = build_successors_table(text)

    >>> table
    {'and': ['to'], 'We': ['came'], 'bad': ['guys'], 'pie': ['.'], ',': ['catch'], '.': ['We'], 'to': ['investigate', 'eat'], 'investigate': [','], 'catch': ['bad'], 'guys': ['and'], 'eat': ['pie'], 'came': ['to']}
	"""    
    table = {}
    prev = '.'
    for word in tokens:
        if prev in table:
            "**FILL THIS IN**"
            # table[prev] += [word]
            table[prev].append(word)            
        else:
            "**FILL THIS IN**"
            table[prev] = [word]
        prev = word
    return table

def construct_sent(word, table):
    """Prints a random sentence starting with word, sampling from table"""
    import random
    result = ' '
    while word not in ['.', '!', '?']:
        "** FILL THIS IN**"
        result += word + ' '
        word = random.choice(table[word])
        return result + word
def shakespeare_tokens(path = 'shakespeare.txt', url = 'http://inst.eecs.berkeley.edu/~cs61a/fa11/shakespeare.txt'):
    """Return the words of Shakespeare's plays as a list"""
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open('shakespeare.txt', encoding='ascii').read().split()
    else:
        shakespeare = urlopen(url)
        return 
# shakespeare.read().decode(encoding='ascii').split()[:2000] # For performance reasons.