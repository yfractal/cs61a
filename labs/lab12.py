# Regular Expressions
import re
def is_identifier(s):
    return True if re.match('[a-zA-Z]+', s) else False

import re
def matches(pattern, s):
            return True if re.match(pattern, s) else False
matches("[a-zA-Z]+", "hello")
True
matches("[A-Za-z_][A-Za-z_0-9]*", "__init__") #this is a proper identifier regex for python
True
matches("[A-Za-z_][A-Za-z_0-9]*", "0imanidentifier")
False
matches("aa+b", "ab")
False
matches("aa+b", "aaaaab")
True
matches("aa*b", "ab")
True
matches("a[bcd]?bc", "abcbcd")    
True


# Calc: our first interpreter!




