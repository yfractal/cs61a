# Take 1: Sets as unordered sequences

def empty(s):
    return s is Rlist.empty

def set_contains(s, v):
    """Return true if set s contains value v as an element.

    >>> set_contains(s, 2)
    True
    >>> set_contains(s, 5)
    False
    """
    if empty(s):
        return False
    if s.first == v:
        return True
    return set_contains(s.rest, v)

def adjoin_set(s, v):
    """Return a set containing all elements of s and element v.

    >>> t = adjoin_set(s, 4)
    >>> t
    Rlist(4, Rlist(1, Rlist(2, Rlist(3))))
    """
    if set_contains(s, v):
        return s
    return Rlist(v, s)

def intersect_set(set1, set2):
    """Return a set containing all elements common to set1 and set2.

    >>> t = adjoin_set(s, 4)
    >>> intersect_set(t, map_rlist(s, lambda x: x*x))
    Rlist(4, Rlist(1))
    """
    return filter_rlist(set1, lambda v: set_contains(set2, v))

def union_set(set1, set2):
    """Return a set containing all elements either in set1 or set2.

    >>> t = adjoin_set(s, 4)
    >>> union_set(t, s)
    Rlist(4, Rlist(1, Rlist(2, Rlist(3))))
    """
    set1_not_set2 = filter_rlist(set1, lambda v: not set_contains(set2, v))
    return extend_rlist(set1_not_set2, set2)

# Take 2: Sets as ordered sequences

def set_contains2(s, v):
    """Return true if set s contains value v as an element.

    >>> set_contains2(s, 2)
    True
    >>> set_contains2(s, 5)
    False
    """
    if empty(s) or s.first > v:
        return False
    if s.first == v:
        return True
    return set_contains2(s.rest, v)

def intersect_set2(set1, set2):
    """Return a set containing all elements common to set1 and set2.

    >>> t = Rlist(2, Rlist(3, Rlist(4)))
    >>> intersect_set2(s, t)
    Rlist(2, Rlist(3))
    """
    if empty(set1) or empty(set2):
        return Rlist.empty
    e1, e2 = set1.first, set2.first
    if e1 == e2:
        return Rlist(e1, intersect_set2(set1.rest, set2.rest))
    if e1 < e2:
        return intersect_set2(set1.rest, set2)
    if e2 < e1:
        return intersect_set2(set1, set2.rest)

# Take 3: Sets as trees

def set_contains3(s, v):
    """Return true if set s contains value v as an element.

    >>> t = Tree(2, Tree(1), Tree(3))
    >>> set_contains3(t, 3)
    True
    >>> set_contains3(t, 0)
    False
    >>> set_contains3(big_tree(20, 60), 34)
    True
    """
    if s is None:
        return False
    if s.entry == v:
        return True
    if s.entry < v:
        return set_contains3(s.right, v)
    if s.entry > v:
        return set_contains3(s.left, v)

def adjoin_set3(s, v):
    """Return a set containing all elements of s and element v.

    >>> b = big_tree(0, 9)
    >>> b
    Tree(4, Tree(1), Tree(7, None, Tree(9)))
    >>> adjoin_set3(b, 5)
    Tree(4, Tree(1), Tree(7, Tree(5), Tree(9)))
    """
    if s is None:
        return Tree(v)
    if s.entry == v:
        return s
    if s.entry < v:
        return Tree(s.entry, s.left, adjoin_set3(s.right, v))
    if s.entry > v:
        return Tree(s.entry, adjoin_set3(s.left, v), s.right)

# From lecture 22: Recursive lists and trees

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

def extend_rlist(s1, s2):
    """Return a list containing the elements of s1 followed by those of s2."""
    if s1 is Rlist.empty:
        return s2
    return Rlist(s1.first, extend_rlist(s1.rest, s2))

def map_rlist(s, fn):
    """Return a list resulting from mapping fn over the elements of s."""
    if s is Rlist.empty:
        return s
    return Rlist(fn(s.first), map_rlist(s.rest, fn))

def filter_rlist(s, fn):
    """Filter the elemenst of s by predicate fn."""
    if s is Rlist.empty:
        return s
    rest = filter_rlist(s.rest, fn)
    if fn(s.first):
        return Rlist(s.first, rest)
    return rest

s = Rlist(1, Rlist(2, Rlist(3))) # A set is an Rlist with no duplicates

class Tree(object):
    """A tree with internal values."""

    def __init__(self, entry, left=None, right=None):
        self.entry = entry
        self.left = left
        self.right = right

    def __repr__(self):
        args = repr(self.entry)
        if self.left or self.right:
            args += ', {0}, {1}'.format(repr(self.left), repr(self.right))
        return 'Tree({0})'.format(args)

def big_tree(left, right):
    """Return a tree of elements between left and right.

    >>> big_tree(0, 12)
    Tree(6, Tree(2, Tree(0), Tree(4)), Tree(10, Tree(8), Tree(12)))
    """
    if left > right:
        return None
    split = left + (right - left)//2
    return Tree(split, big_tree(left, split-2), big_tree(split+2, right))