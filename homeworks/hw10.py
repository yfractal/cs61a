# Name:
# Login:
# TA:
# Section:
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


def read_eval_print_loop():
    """Run a read-eval-print loop for the Brackulator language."""
    global Pair, nil
    from scheme_reader import Pair, nil
    from scalc import calc_eval

    while True:
        try:
            src = tokenize(input('> '))
            while len(src) > 0:
              expression = brack_read(src)
              print(calc_eval(expression))
        except (SyntaxError, ValueError, TypeError, ZeroDivisionError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc.
            return



BRACKETS = {('[', ']'): '+',
            ('(', ')'): '-',
            ('<', '>'): '*',
            ('{', '}'): '/'}
PRE_OP_DIC ={'[':'+',
             '(':'-',
             '<':'*',
             '{':'/' }            
LEFT_RIGHT = {left:right for left, right in BRACKETS.keys()}
ALL_BRACKETS = set(b for bs in BRACKETS for b in bs)
PRE_TOKENS = ['[','(','<','{']
PAIR = [('(',')'),('{','}'),('[',']'),('<','>')]
POST_TOKEN = [')','}',']','>']

# Q1.
print(ALL_BRACKETS)

def tokenize(line):
    """Convert a string into a list of tokens.

    >>> tokenize('<[2{12.5 6.0}](3 -4 5)>')
    ['<', '[', 2, '{', 12.5, 6.0, '}', ']', '(', 3, -4, 5, ')', '>']

    >>> tokenize('2.3.4')
    Traceback (most recent call last):
        ...
    ValueError: invalid token 2.3.4

    >>> tokenize('?')
    Traceback (most recent call last):
        ...
    ValueError: invalid token ?

    >>> tokenize('hello')
    Traceback (most recent call last):
        ...
    ValueError: invalid token hello

    >>> tokenize('<(GO BEARS)>')
    Traceback (most recent call last):
        ...
    ValueError: invalid token GO
    """
    "*** YOUR CODE HERE ***"
    spaced = line
    for token in ALL_BRACKETS:
        spaced = spaced.replace(token,' '+token + ' ')
    spaced = spaced.split()

    i = 0

    for t in spaced:
        if t not in ALL_BRACKETS:
            to_num = coerce_to_number(t)
            if to_num == None:
                raise ValueError('invalid token ' + t)
            else:
                spaced[i] = to_num
        i += 1
            # try:
            #     spaced[i] = int(t)
            # except(ValueError):
            #     try:
            #         spaced[i] = float(t)
            #     except(ValueError):
            #         raise ValueError('invalid token ' + t)
    return spaced


def coerce_to_number(token):
    """Coerce a string to a number or return None.

    >>> coerce_to_number('-2.3')
    -2.3
    >>> print(coerce_to_number('('))
    None
    """
    try:
        return int(token)
    except (TypeError, ValueError):
        try:
            return float(token)
        except (TypeError, ValueError):
            return None

# # Q2.
def is_post(token):
    return token in POST_TOKEN
def is_pre(token):
    return token in PRE_TOKENS
def isvalid(tokens):
    """Return whether some prefix of tokens represent a valid Brackulator
    expression. Tokens in that expression are removed from tokens as a side
    effect.

    >>> isvalid(tokenize('([])'))
    True
    >>> isvalid(tokenize('([]')) # Missing right bracket
    False
    >>> isvalid(tokenize('[)]')) # Extra right bracket
    False
    >>> isvalid(tokenize('([)]')) # Improper nesting
    False
    >>> isvalid(tokenize('')) # No expression
    False
    >>> isvalid(tokenize('100'))
    True
    >>> isvalid(tokenize('<(( [{}] [{}] ))>'))
    True
    >>> isvalid(tokenize('<[2{12 6}](3 4 5)>'))
    True
    >>> isvalid(tokenize('()()')) # More than one expression is ok
    True
    >>> isvalid(tokenize('[])')) # Junk after a valid expression is ok
    True
    """
    "*** YOUR CODE HERE ***"

    def is_match(pre,post):
        return (pre,post) in PAIR
    if len(tokens) == 0:
        return False
    match_stack = []
    for token in tokens:
        if type(token) != int and type(token) != float:
            match_stack.append(token)
        if is_post(token):
            if len(match_stack) >= 2:
                post = match_stack.pop()
                pre = match_stack.pop()
                if not is_match(pre,post):
                    return False

    while len(match_stack) != 0:
        if not is_post(match_stack.pop()):
            return False
    return match_stack == []

# # Q3.

def brack_read(tokens):
    """Return an expression tree for the first well-formed Brackulator
    expression in tokens. Tokens in that expression are removed from tokens as
    a side effect.

    >>> brack_read(tokenize('100'))
    100
    >>> brack_read(tokenize('([])'))
    Pair('-', Pair(Pair('+', nil), nil))
    >>> print(brack_read(tokenize('<[2{12 6}](3 4 5)>')))
    (* (+ 2 (/ 12 6)) (- 3 4 5))
    >>> brack_read(tokenize('(1)(1)')) # More than one expression is ok
    Pair('-', Pair(1, nil))
    >>> brack_read(tokenize('[])')) # Junk after a valid expression is ok
    Pair('+', nil)

    >>> brack_read(tokenize('([]')) # Missing right bracket
    Traceback (most recent call last):
        ...
    SyntaxError: unexpected end of line

    >>> brack_read(tokenize('[)]')) # Extra right bracket
    Traceback (most recent call last):
        ...
    SyntaxError: unexpected )

    >>> brack_read(tokenize('([)]')) # Improper nesting
    Traceback (most recent call last):
        ...
    SyntaxError: unexpected )

    >>> brack_read(tokenize('')) # No expression
    Traceback (most recent call last):
        ...
    SyntaxError: unexpected end of line
    """
    def analyze(tokens):
        if len(tokens) == 0:
            return nil
        token = tokens.pop(0)
        if token in (int,float):
            return token
        if token in POST_TOKEN:
            return analyze(tokens)
        if is_pre(token):
            return Pair(PRE_OP_DIC[token],analyze_operands(tokens,token))
    def analyze_operands(tokens,pre_op):
        args = []
        token = tokens.pop(0)
        while token != LEFT_RIGHT[pre_op]:
            args.append(token)
            token = tokens.pop(0)
        return Pair(PRE_OP_DIC[args[0]],analyze(args[1:]))

    return analyze(tokens)

r1 = brack_read(tokenize('([])'))
print("should be:\nPair('-', Pair(Pair('+', nil), nil))")


# t4 = tokenize('(1 2)')
# r4 = brack_read(t4)
# print("r4 should be ")
# print("(- 1 2)")
# print(r4)

# print("r1 is pending")
# t1 = tokenize('100')
# r1 = brack_read(t1) 

# t2 = tokenize('()')
# r2 = brack_read(t2)

# # # Pair('-', Pair(Pair('+', nil), nil))
# t3 = tokenize('([])')        
# r3 = brack_read(t3)
# print("r3 should be")
# print("Pair('-', Pair(Pair('+', nil), nil))")

# t4 = tokenize('<[2{12 6}](3 4 5)>')
# r4 = brack_read(t4)
# print("r4 should be")
# print("(* (+ 2 (/ 12 6)) (- 3 4 5))")
# t5 = tokenize('(1 2)')
# r5 = brack_read(t5)

# # Q4.

# from urllib.request import urlopen

# def puzzle_4():
#     """Return the soluton to puzzle 4."""
#     "*** YOUR CODE HERE ***"


