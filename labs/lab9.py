from tree_ops import *
# print(kennedy)
tmp = kennedy
print_tree(tmp)
print_tree(tmp.children()[0].children()[1])

def square(n):
    return n * n

def square_tree(tree):
    return make_tree(square(datum(tree)), square_forest(children(tree)))

def square_forest(forest):
    if forest == []:
       return []
    else:
       return [square_tree(forest[0])] + square_forest(forest[1:])

def tree_map(f,tree):
    return make_tree( 
        f( datum(tree))  ,
            forest_map(f, children(tree) )
            ) 

def forest_map(f,forest):
    if forest == []:
        return []
    else:
        return [tree_map(f, forest[0]) ] +  forest_map(f,forest[1:])

print_tree(t)
st = tree_map(square, t)
print_tree(st)

def max_of_tree(t):
    return max( datum(t) ,max_of_forest( children(t)) )

def max_of_forest( forest):
    if forest == []:
        return -10000
    else:
        return max(  max_of_tree(forest[0])  ,max_of_forest(forest[1:]) )
print(max_of_tree(t))

# Question 4:
def sum_of_bin_tree(b_t):
    if b_t == None:
        return 0
    return sum_3(
          b_datum( b_t) ,
          sum_of_bin_tree(b_left_branch(b_t)) ,
          sum_of_bin_tree(b_right_branch(b_t)) 
       )

def sum_3(a,b,c):
    return a + b + c

print("Q4")
print(sum_of_bin_tree(b_t))

# Question 5:

def  count_leaves(b_t):
    if b_t == None:
        return 0
    elif b_leaf(b_t):
        return 1
    return count_leaves(b_left_branch(b_t)) + count_leaves(b_right_branch(b_t))
print("Q5")
print( count_leaves(b_t) )