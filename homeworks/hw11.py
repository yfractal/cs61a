# Name:
# Login:
# TA:
# Section:
# Q1.

# def num_splits(s, d):
#     """Return the number of ways in which s can be partitioned into two
#     sublists that have sums within d of each other.
#     >>> s1 = {1,5,4}
#     >>> num_splits(s1, 0)  # splits to {1, 4} and {5}
#     1
#     >>> s2 = {6,1,3}
#     >>> num_splits(s2, 1)  # no split possible
#     0
#     >>> s3 = {-2,1,3}
#     >>> num_splits(s3, 2) # {-2, 3} {1} and {-2, 1, 3} {}
#     2
#     >>> s4 = {1,4,6,8,2,9,5}
#     >>> num_splits({1, 4, 6, 8, 2, 9, 5}, 3)
#     12

#     Hint: You can split a set s into one arbitrary element and the rest with:

#     k = s.pop()
#     rest = set(s)
#     s.add(k)

#     After which s is unchanged, and {k}.union(rest) == s
#     """
#     "*** YOUR CODE HERE ***"
#     # print("s is")
#     # print(s)
#     def sum_set(s):
#         if s == None:
#             return 0
#         else:
#             return sum(s)

#     def num_splits_h(s1,s2,d):
#         # print("s1 is:")
#         # print(s1)
#         # print("s2 is:")
#         # print(s2)
#         sum_s1 = sum_set(s1)
#         sum_s2 = sum_set(s2)

#         if s1 == None:
#             if sum_s1 - sum_s2 == d:
#                 return 1
#             else:
#                 return 0

#         if sum_s1 - sum_s2 == d:
#             increase = 1
#         else:
#             increase = 0
#         t = s1.pop()
#         return increase + num_splits_h({t}.union(s1),s2,d) + num_splits_h(s1,{t}.union(s2),d)

#     return num_splits_h(s,set(),d)

# r = num_splits({1, 1}, 0)  # splits to {1, 4} and {5}


    # def num_splits_h(left_s,right_s,d):
    #     if len(right_s) == 1:
    #         if sum(left_s)-(sum(right_s))== d:
    #             return 1
    #         else :
    #             return 0
    #     if len(right_s) == 0:
    #         return 0
    #     times = 0
    #     right_c = right_s.copy()
    #     i = 0
    #     while len(right_c) != 0:
    #         i += 1 #record which element is poped out
    #         this_turn = 0
    #         t = right_c.pop()
    #         sum_left = sum(left_s)
    #         sum_right = sum(right_s)
    #         # print("len of left_s")
    #         # print(len(left_s))
    #         if sum_left + t - (sum_right - t) == d:
    #             this_turn += 1

    #         if len(left_s) == 0:
    #             next_left_s = set({t})
    #             times += num_splits_h(next_left_s,right_s - {t},d)
    #         else:
    #             left_s.add(t)
    #             times += num_splits_h(left_s,right_s - {t},d) + this_turn
    #     return times
    # return num_splits_h(set({}),s,d)
# num_splits({1, 5, 4}, 0)    
# Q2

def num_trees(n):
    """How many full binary trees have exactly n leaves? E.g.,

    1   2        3       3    ...
    *   *        *       *
       / \      / \     / \
      *   *    *   *   *   *
              / \         / \
             *   *       *   *

    >>> num_trees(1)
    1
    >>> num_trees(2)
    1
    >>> num_trees(3)
    2
    >>> num_trees(8)
    429

    """
    "*** YOUR CODE HERE ***"

    if n <= 2:
        return 1
    s = 0
    i = 1
    while i <= n - 1:
        s += num_trees(i) * num_trees(n - i)
        i += 1
    return s
# # Q3.

def mario_number(level):
    """Return the number of ways that Mario can perform a sequence of steps
    or jumps to reach the end of the level without ever landing in a Piranha
    plant. Assume that every level begins and ends with a space.

    >>> mario_number(' P P ')   # jump, jump
    1
    >>> mario_number(' P P  ')   # jump, jump, step
    1
    >>> mario_number('  P P ')  # step, jump, jump
    1
    >>> mario_number('   P P ') # step, step, jump, jump or jump, jump, jump
    2
    >>> mario_number(' P PP ')  # Mario cannot jump two plants
    0
    >>> mario_number('    ')    # step, jump ; jump, step ; step, step, step
    3
    >>> mario_number('    P    ')
    9
    >>> mario_number('   P    P P   P  P P    P     P ')
    180
    """
    "*** YOUR CODE HERE ***"
    if len(level) == 1:
        # reach the end
        return 1
    if len(level) == 0:
        # jump out ...
        return 0

    if level[0] == "P":
        # eaten by a fish...
        return 0

    if len(level) >= 2:
        return mario_number(level[1:]) + mario_number(level[2:])
    else:
        return mario_number(level[1:])
# r = mario_number(' P P ')   # jump, jump
# print(r)

# Q4.

maze1 = """
******** *
* *      *
* * ******
* *   *  *
* *** *  *
*   * *  *
*** * *  *
*        *
* ********
"""

maze2 = """
********** *
*      *   *
*** **** * *
*      * * *
* **** * * *
*      *** *
****** *   *
*        * *
* **********
"""

def print_path(maze):
    """Print a path through a maze.

    >>> print_path(maze1)
    ********.*
    * *......*
    * *.******
    * *...*  *
    * ***.*  *
    *   *.*  *
    *** *.*  *
    *.....   *
    *.********

    >>> print_path(maze2)
    **********.*
    *      *  .*
    *** **** *.*
    *      * *.*
    * **** * *.*
    *      ***.*
    ****** *...*
    *........* *
    *.**********
    """
    "*** YOUR CODE HERE ***"
    LEN = 12
    # print(len("********** *"))
    maze_array = []
    def maze_to_array(maze):
        line = []
        for s in maze:
            if s != "\n":
                line.append(s)
            else:
                maze_array.append(line)
                line = []


    def a_way(x,y):
        print("x is " + str(x)+"y is  " + str(y))
        if y >= LEN -1 or x >= 9 - 1:
            return False

        if maze_array[y][x] == "*":
            return False
        elif maze_array[y][x] == ".":
            return False
        else:
            print("walk in ")
            return True

    def walk(x,y):
        # walk to this block
        maze_array[y][x] = "."


    def explore(x,y):
        print("in ex")
        print("x is:",x,"y is:",y)
        if x == 1 and y == 8:
            return True

        if a_way(x+1,y):
            walk(x+1,y)
            return explore(x+1,y)

        if a_way(x-1,y):
            walk(x-1,y)
            return explore(x-1,y)

        if a_way(x,y+1):
            walk(x,y+1)
            return explore(x,y+1)
        if a_way(x,y-1):
            walk(x,y-1)
            return explore(x,y-1)


    maze_to_array(maze)
    maze_array.pop(0)

    i = 0
    while i < LEN:
        if a_way(i,0):
            if explore(i,0):
                break
        i += 1

    return maze_array


r = print_path(maze1)
print(r)

# class Leaf(object):
#     def __init__(self, letter, weight):
#         self.letter = letter
#         self.weight = weight

# class Tree(object):
#     def __init__(self, left, right):
#         self.left = left
#         self.right = right
#         self.weight = left.weight + right.weight

# A = Leaf('a', 8)
# BCD = Tree(Leaf('b', 3), Tree(Leaf('c', 1), Leaf('d', 1)))
# EFGH = Tree(Tree(Leaf('e', 1), Leaf('f', 1)),
#             Tree(Leaf('g', 1), Leaf('h', 1)))
# AH = Tree(A, Tree(BCD, EFGH))

# # Q5.

# def decode(tree, code):
#     """Decode a list of 0's and 1's using the Huffman encoding tree.

#     >>> decode(AH, [1, 0, 0, 0, 1, 0, 1, 0])
#     'bac'
#     """
#     word = ''
#     while code != []:
#         word += decode_one(tree, code)
#     return word

# def decode_one(tree, code):
#     """Decode and remove the first letter in code, using tree.

#     >>> code = [1, 0, 0, 0, 1, 0, 1, 0]
#     >>> decode_one(AH, code)
#     'b'
#     >>> code
#     [0, 1, 0, 1, 0]
#     """
#     "*** YOUR CODE HERE ***"

# # Q6.

# def encodings(tree):
#     """Return all encodings in a tree as a dict from letters to bit lists.

#     >>> e = encodings(AH)
#     >>> e['a']
#     [0]
#     >>> e['c']
#     [1, 0, 1, 0]
#     >>> e['h']
#     [1, 1, 1, 1]
#     """
#     "*** YOUR CODE HERE ***"

# # Q7.

# def huffman(elements):
#     """Return an optimal Huffman encoding tree of elements, a sorted lists.

#     >>> h = huffman([Leaf('c', 1), Leaf('d', 1), Leaf('b', 3), Leaf('a', 8)])
#     >>> for letter, code in sorted(encodings(h).items()): print(letter + ':', code)
#     a: [1]
#     b: [0, 1]
#     c: [0, 0, 0]
#     d: [0, 0, 1]
#     """
#     "*** YOUR CODE HERE ***"

