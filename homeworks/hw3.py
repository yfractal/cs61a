# Name:
# Login:
# TA:
# Section:
# Q1.

square = lambda x: x ** 2
def smooth(f, dx):
    """Returns the smoothed version of f, g where

    g(x) = (f(x - dx) + f(x) + f(x + dx)) / 3

    >>> square = lambda x: x ** 2
    >>> round(smooth(square, 1)(0), 3)
    0.667
    """
    "*** YOUR CODE HERE ***"
    return lambda x: (f(x - dx) + f(x) + f(x + dx)) /3

def n_fold_smooth(f, dx, n):
    """Returns the n-fold smoothed version of f

    >>> square = lambda x: x ** 2
    >>> round(n_fold_smooth(square, 1, 3)(0), 3)
    1.901
    """
    "*** YOUR CODE HERE ***"
    def repeated(f, n):
        def h(x):
            i = 1
            t = x
            while i <= n:
                t = f(t)
                i += 1
            return t
        return h
    return repeated(lambda x: smooth(f,dx)(x),n)    
# Q2.

def iterative_continued_frac(n_term, d_term, k):
    """Returns the k-term continued fraction with numerators defined by n_term
    and denominators defined by d_term.

    >>> # golden ratio
    ... round(iterative_continued_frac(lambda x: 1, lambda x: 1, 8), 3)
    0.618
    >>> # 1 / (1 + (2 / (2 + (3 / (3 + (4 / 4))))))
    ... round(iterative_continued_frac(lambda x: x, lambda x: x, 4), 6)
    0.578947
    """
    "*** YOUR CODE HERE ***"
    i = k
    while i >= 1:
        if i == k:
            t = n_term(i) / d_term(i)
        else :
            t = n_term(i) / (d_term(i) + t)
        i -= 1
    return t            

def recursive_continued_frac(n_term, d_term, k):
    """Returns the k-term continued fraction with numerators defined by n_term
    and denominators defined by d_term.

    >>> # golden ratio
    ... round(recursive_continued_frac(lambda x: 1, lambda x: 1, 8), 3)
    0.618
    >>> # 1 / (1 + (2 / (2 + (3 / (3 + (4 / 4))))))
    ... round(recursive_continued_frac(lambda x: x, lambda x: x, 4), 6)
    0.578947
    """
    "*** YOUR CODE HERE ***"
    # def frac_helper(n_term,d_term,k):
    def frac_helper(n):
        if n == k:
            return n_term(n) / d_term(n)
        return n_term(n) / ( d_term(n) + frac_helper(n+1) )
    return frac_helper(1)

# Q3.

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.
    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    i = 4
    # n = 4
    g_n_1 = 3
    g_n_2 = 2
    g_n_3 = 1
    while i <= n:
        g_n = g_n_1 + 2 * g_n_2 + 3 * g_n_3

        g_n_3,g_n_2,g_n_1 = g_n_2,g_n_1,g_n
        i += 1

    return g_n
# Q4.

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
    return lambda n:1 if n == 1 else mul(n,make_anonymous_factorial()(n-1))

