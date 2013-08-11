"""Lab10 starter code"""
from sets import *

# Q1
def is_subset(set1, set2):
    """Returns True if set2 is a subset of set1.

    >>> set1 = Rlist(1, Rlist(4, Rlist(2, Rlist(5))))
    >>> set2 = Rlist(1, Rlist(2, Rlist(4)))
    >>> is_subset(set1, set2)
    True
    >>> set3 = Rlist(1, Rlist(2, Rlist(3, Rlist(4))))
    >>> is_subset(set1, set3)
    False
    """
    if empty(set2):
        return True
    if not set_contains(set1,set2.first):
        return False
    return is_subset(set1,set2.rest)

# Q2
def rlist_to_set(rlist):
    """Returns a set that contains unique elements in the given rlist.

    >>> r = Rlist(1, Rlist(2, Rlist(2, Rlist(1))))
    >>> rlist_to_set(r)
    Rlist(2, Rlist(1))
    """
    # r_set = Rlist(rlist.first)
    # rlist = rlist.rest
    # while not empty(rlist):
    #     if not set_contains(r_set,rlist.first):
    #         r_set = Rlist(rlist.first,r_set)
    #     rlist = rlist.rest
    # return r_set        
    if empty(rlist):
        return rlist
    elif set_contains(rlist.rest, rlist.first):
        return rlist_to_set(rlist.rest)
    else:
        return Rlist(rlist.first, rlist_to_set(rlist.rest))    

# Q3
def rlist_to_set_mut(rlist):
    """Mutates the original Rlist by removing duplicate items.

    >>> r = Rlist(1, Rlist(2, Rlist(2, Rlist(1))))
    >>> rlist_to_set_mut(r)
    >>> r
    Rlist(2, Rlist(1))
    """
    if len(rlist) <= 1:
        return 
    elif set_contains(rlist.rest, rlist.first):
        rlist_to_set_mut(rlist.rest)
        rlist.first, rlist.rest  = rlist.rest.first, rlist.rest.rest
    else:
        rlist_to_set_mut(rlist.rest)

# Q5
def exclusive_or(set1, set2):
    """Returns a set containing elements in set1 or set2, but not
    elements that appear in both.

    >>> set1 = Rlist(1, Rlist(2, Rlist(3)))
    >>> set2 = Rlist(1, Rlist(3, Rlist(4)))
    >>> exclusive_or(set1, set2)
    Rlist(2, Rlist(4))
    """
    if empty(set1):
        return set2
    if empty(set2):
        return set1
    if set1.first < set2.first:
        # if set_contains(set2,set1.first):
        #     return exclusive_or(set1.rest,set2)
        # else:
        return Rlist(set1.first,exclusive_or(set1.rest,set2))
    if set1.first > set2.first:
        # if set_contains(set1,set2.first):
        #     return exclusive_or(set1,set2.rest)
        # else:
        return Rlist(set2.first,exclusive_or(set1,set2.rest))
    return exclusive_or(set1.rest,set2.rest)        

# Q8
def max_set(s):
    """Finds the largest element in a set that is implemented as a 
    binary search tree.
    >>> s = Tree(4,
    ...            Tree(2,
    ...                   Tree(1)),
    ...            Tree(5,
    ...                   None,
    ...                   Tree(6)))
    >>> max_set(s)
    6
    """
    if s.right == None:
        return s.entry
    return max_set(s.right)
