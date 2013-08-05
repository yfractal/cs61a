#Tree Representation for Lab 9

#Representation for General Trees

class Tree(object):
    def __init__(self, entry, kids):
        self.entry = entry
        self.kids = kids

    def datum(self):
        return self.entry

    def children(self):
        return self.kids

    def leaf(self):
        return self.children == []

    def listify_tree(self):
        tree_ls = [self.entry]
        children_ls = []
        for tree in self.kids:
            sub_tree_ls = [tree.listify_tree()]
            children_ls += sub_tree_ls
        tree_ls.append(children_ls)
        return tree_ls

#constructor        
def make_tree(datum, children):
    return Tree(datum, children)
    
#selectors    
def datum(tree):
    return tree.datum()
    
def children(tree):
    return tree.children()

#leaf returns true/false, if the node has no children    
def leaf(tree):
    return tree.children == []
    
#prints out a tree in list form
def print_tree(tree):
    print(tree.listify_tree())


#Representation for Binary Trees:


class Binary_Tree(object):
    def __init__(self, entry, left=None, right=None):
                self.entry = entry
                self.left = left
                self.right = right

    def datum(self):
        return self.entry

    def left_branch(self):
        return self.left

    def right_branch(self):
        return self.right

    def leaf(self):
        return self.right == None and self.left == None
        
    def __repr__(self):
                args = repr(self.entry)
                if self.left or self.right:
                        args += ', {0}, {1}'.format(repr(self.left), repr(self.right))
                return 'Tree({0})'.format(args)
           

#constructor
def make_b_tree(datum, left_branch=None, right_branch=None):
    return Binary_Tree(datum, left_branch, right_branch)
    
#selectors    
def b_datum(bin_tree):
    return bin_tree.datum()
    
def b_left_branch(bin_tree):
    return bin_tree.left_branch()

def b_right_branch(bin_tree):
    return bin_tree.right_branch()
    
#leaf check, returns true/false if the node is a leaf    
def b_leaf(bin_tree):
    return bin_tree.leaf()

#prints out a binary tree    
def print_b_tree(bin_tree):
    print(bin_tree)
    

    
#trees to work with for lab

#kennedy string tree

kennedy = make_tree('Joseph', [make_tree('John f', [make_tree('John Jr', []), make_tree('Caroline', [])]), make_tree('Robert', [make_tree('Kathleen', [])]), make_tree('Edward', [])])

#General Integer Tree

t = make_tree(4, [make_tree(2, [make_tree(8, [make_tree(7, [])]), make_tree(3, [make_tree(1, []), make_tree(6, [])])]), make_tree(1, [make_tree(5, [])]), make_tree(3, [make_tree(2, []), make_tree(9, [])])])

#Binary Integer Tree

b_t = make_b_tree(3, make_b_tree(7, make_b_tree(8, make_b_tree(6), make_b_tree(2)), make_b_tree(2)), make_b_tree(2, make_b_tree(5), make_b_tree(3, make_b_tree(9), make_b_tree(4))))
