"""This module implements the core Scheme interpreter functions, including the
eval/apply mutual recurrence, environment model, and read-eval-print loop.
"""

from scheme_primitives import *
from scheme_reader import *
from ucb import main, trace

##############
# Eval/Apply #
##############

def scheme_eval(expr, env):
    """Evaluate Scheme expression EXPR in environment ENV.

    >>> expr = read_line("(+ 2 2)")
    >>> expr
    Pair('+', Pair(2, Pair(2, nil)))
    >>> scheme_eval(expr, create_global_frame())
    4
    """
    # print("expr is:",expr)

    if expr is None:
        raise SchemeError("Cannot evaluate an undefined expression.")
    if scheme_symbolp(expr):
        r = env.lookup(expr)
        if r == None:
            return expr
        return r
    elif scheme_atomp(expr):
        return expr

    # All non-atomic expressions are lists.
    if not scheme_listp(expr):
        raise SchemeError("malformed list: {0}".format(str(expr)))
    first, rest = expr.first, expr.second
    # Evaluate Combinations
    if first in LOGIC_FORMS:
        # in begin, lambda form
        # return scheme_eval(LOGIC_FORMS[first](rest, env), env)
        return scheme_eval(LOGIC_FORMS[first](rest, env), env)
    elif first == "lambda":
        return do_lambda_form(rest, env)
    elif first == "mu":
        return do_mu_form(rest)
    elif first == "define":
        return do_define_form(rest, env)
    elif first == "quote":
        return do_quote_form(rest)
    elif first == "let":
        expr, env = do_let_form(rest, env)
        return scheme_eval(expr, env)
    else:
        # somethint is wrong here...

        procedure = scheme_eval(first, env)
        args = rest.map(lambda operand: scheme_eval(operand, env))
        # print("before call scheme_apply")
        # print("procedure:",procedure)
        return scheme_apply(procedure, args, env)

def scheme_apply(procedure, args, env):
    """Apply Scheme PROCEDURE to argument values ARGS in environment ENV."""
    # suppose this is wright
    # print("procedure is in scheme_apply")
    # print(procedure)
    if isinstance(procedure, PrimitiveProcedure):
        return apply_primitive(procedure, args, env)
    elif isinstance(procedure, LambdaProcedure):
        "*** YOUR CODE HERE ***"
        formals = procedure.formals
        f = env.make_call_frame(formals,args)
        # print("procedure.body")
        # print(procedure.body)
        return scheme_eval(procedure.body,f)
        # Create a new Frame, with all formal parameters bound to their argument values.
        # Evaluate the body of procedure in the environment represented by this new frame.
        # Return the value of calling procedure.

    elif isinstance(procedure, MuProcedure):
        "*** YOUR CODE HERE ***"
    else:
        raise SchemeError("Cannot call {0}".format(str(procedure)))



def apply_primitive(procedure, args, env):
    """Apply PrimitiveProcedure PROCEDURE to a Scheme list of ARGS in ENV.

    >>> env = create_global_frame()
    >>> plus = env.bindings["+"]
    >>> twos = Pair(2, Pair(2, nil))
    >>> apply_primitive(plus, twos, env)
    4
    """
    "*** YOUR CODE HERE ***"
    # Convert the Scheme list to a Python list of arguments.
    def scheme_list_to_python_list(s_l):
        p_list = []
        while s_l.second != nil:
            p_list += [s_l.first]
            s_l = s_l.second
        p_list += [s_l.first]
        return p_list
    python_list = scheme_list_to_python_list(args)
    if procedure.use_env:
        # env just the last paramter of the function...
        python_list += [env]
    try:
        r = procedure.fn(*python_list)
    except TypeError:
        raise SchemeError("in apply_primitive") 
    return r

################
# Environments #
################

class Frame(object):
    """An environment frame binds Scheme symbols to Scheme values."""

    def __init__(self, parent):
        """An empty frame with a PARENT frame (that may be None)."""
        self.bindings = {}
        self.parent = parent

    def __repr__(self):
        if self.parent is None:
            return "<Global Frame>"
        else:
            s = sorted('{0}: {1}'.format(k,v) for k,v in self.bindings.items())
            return "<{{{0}}} -> {1}>".format(', '.join(s), repr(self.parent))

    def lookup(self, symbol):
        """Return the value bound to SYMBOL.  Errors if SYMBOL is not found."""
        "*** YOUR CODE HERE ***"
        if self == None:
            raise SchemeError("no such symbol in frame")
        if symbol in self.bindings:
            return self.bindings[symbol]
        if self.parent != None:
            return self.parent.lookup(symbol)


    def global_frame(self):
        """The global environment at the root of the parent chain."""
        e = self
        while e.parent is not None:
            e = e.parent
        return e

    def make_call_frame(self, formals, vals):
        """Return a new local frame whose parent is SELF, in which the symbols
        in the Scheme formal parameter list FORMALS are bound to the Scheme
        values in the Scheme value list VALS.

        >>> env = create_global_frame()
        >>> formals, vals = read_line("(a b c)"), read_line("(1 2 3)")
        >>> env.make_call_frame(formals, vals)
        <{a: 1, b: 2, c: 3} -> <Global Frame>>
        """
        frame = Frame(self)
        "*** YOUR CODE HERE ***"
        i = 0
        while i < len(formals):
            frame.bindings[formals[i]] = vals[i]
            i += 1
        return frame

    def define(self, sym, val):
        """Define Scheme symbol SYM to have value VAL in SELF."""
        self.bindings[sym] = val

class LambdaProcedure(object):
    """A procedure defined by a lambda expression or the complex define form."""

    def __init__(self, formals, body, env):
        """A procedure whose formal parameter list is FORMALS (a Scheme list),
        whose body is the single Scheme expression BODY, and whose parent
        environment is the Frame ENV.  A lambda expression containing multiple
        expressions, such as (lambda (x) (display x) (+ x 1)) can be handled by
        using (begin (display x) (+ x 1)) as the body."""
        self.formals = formals
        self.body = body
        self.env = env

    def __str__(self):
        return "(lambda {0} {1})".format(str(self.formals), str(self.body))

    def __repr__(self):
        args = (self.formals, self.body, self.env)
        return "LambdaProcedure({0}, {1}, {2})".format(*(repr(a) for a in args))

class MuProcedure(object):
    """A procedure defined by a mu expression, which has dynamic scope.
     _________________
    < Scheme is cool! >
     -----------------
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||
    """

    def __init__(self, formals, body):
        """A procedure whose formal parameter list is FORMALS (a Scheme list),
        whose body is the single Scheme expression BODY.  A mu expression
        containing multiple expressions, such as (mu (x) (display x) (+ x 1))
        can be handled by using (begin (display x) (+ x 1)) as the body."""
        self.formals = formals
        self.body = body

    def __str__(self):
        return "(mu {0} {1})".format(str(self.formals), str(self.body))

    def __repr__(self):
        args = (self.formals, self.body)
        return "MuProcedure({0}, {1})".format(*(repr(a) for a in args))


#################
# Special forms #
#################

def do_lambda_form(vals, env):
    # env is parent frame
    """Evaluate a lambda form with parameters VALS in environment ENV."""
    check_form(vals, 2)
    formals = vals[0]
    check_formals(formals)
    "*** YOUR CODE HERE ***"
    # print("env in do_lambda_form")
    # print(env)
    body = vals[1]
    # print("body in lambda")
    # print(body)
    if len(vals) == 3:
        body = Pair("begin",vals.second)
    return LambdaProcedure(formals,body,env)

def do_mu_form(vals):
    """Evaluate a mu form with parameters VALS."""
    check_form(vals, 2)
    formals = vals[0]
    check_formals(formals)
    "*** YOUR CODE HERE ***"


def do_define_form(vals, env):
    """Evaluate a define form with parameters VALS in environment ENV."""
    check_form(vals, 2)
    target = vals[0]
    if scheme_symbolp(target):
        check_form(vals, 2, 2)
        "*** YOUR CODE HERE ***"
        env.bindings[target] = scheme_eval(vals[1],env)
        # or scheme_eval(vals[1],env)??
    elif isinstance(target, Pair):
        "*** YOUR CODE HERE ***"
        params = vals.first.second
        # print("target",target)
        target = target[0]
        l = Pair("lambda",Pair(params,vals.second))
        # print(l)
        env.bindings[target] = scheme_eval(l,env)
    else:
        raise SchemeError("bad argument to define")

def do_quote_form(vals):
    """Evaluate a quote form with parameters VALS."""
    check_form(vals, 1, 1)
    "*** YOUR CODE HERE ***"
    return vals.first

def do_let_form(vals, env):
    """Evaluate a let form with parameters VALS in environment ENV."""
    check_form(vals, 2)
    bindings = vals[0]
    exprs = vals.second
    if not scheme_listp(bindings):
        raise SchemeError("bad bindings list in let form")

    # Add a frame containing bindings
    names, vals = nil, nil
    "*** YOUR CODE HERE ***"
    new_env = env.make_call_frame(names, vals)

    # Evaluate all but the last expression after bindings, and return the last
    last = len(exprs)-1
    for i in range(0, last):
        scheme_eval(exprs[i], new_env)
    return exprs[last], new_env

#########################
# Logical Special Forms #
#########################

def do_if_form(vals, env):
    """Evaluate if form with parameters VALS in environment ENV."""
    check_form(vals, 3, 3)
    "*** YOUR CODE HERE ***"
    condition = vals[0]
    if len(vals) < 3:
        raise SchemeError("too few operands in form")
    if scheme_eval(condition,env):
        return scheme_eval(vals[1],env)
    else:
        return scheme_eval(vals[2],env)

def do_and_form(vals, env):
    """Evaluate short-circuited and with parameters VALS in environment ENV."""
    "*** YOUR CODE HERE ***"

def do_or_form(vals, env):
    """Evaluate short-circuited or with parameters VALS in environment ENV."""
    "*** YOUR CODE HERE ***"

def do_cond_form(vals, env):
    """Evaluate cond form with parameters VALS in environment ENV."""
    num_clauses = len(vals)
    for i, clause in enumerate(vals):
        check_form(clause, 1)
        if clause.first == "else":
            if i < num_clauses-1:
                raise SchemeError("else must be last")
            test = True
            if clause.second is nil:
                raise SchemeError("badly formed else clause")
        else:
            test = scheme_eval(clause.first, env)
            # false if false ,else is true
        if scheme_true(test):
            "*** YOUR CODE HERE ***"
            # else condition
            if clause.second == nil:
                # no clause...
                return True
            if len(clause) == 3:
                return scheme_eval(Pair("begin",clause.second),env)
            r =  scheme_eval(clause.second.first,env)
            return r

def do_begin_form(vals, env):
    """Evaluate begin form with parameters VALS in environment ENV."""
    check_form(vals, 1)
    "*** YOUR CODE HERE ***"
    # scm> (begin (display 3) (newline) (+ 2 3))
    #     3
    #     5
    # above case without 3
    # pending...!!!
    # get last
    while vals.second != nil:
        vals = vals.second
    # the return eval
    return scheme_eval(Pair("quote",vals),env)

LOGIC_FORMS = {
        "and": do_and_form,
        "or": do_or_form,
        "if": do_if_form,
        "cond": do_cond_form,
        "begin": do_begin_form,
        }

# Utility methods for checking the structure of Scheme programs

def check_form(expr, min, max = None):
    """Check EXPR (default SELF.expr) is a proper list whose length is
    at least MIN and no more than MAX (default: no maximum). Raises
    a SchemeError if this is not the case."""
    if not scheme_listp(expr):
        raise SchemeError("badly formed expression: " + str(expr))
    length = len(expr)
    if length < min:
        raise SchemeError("too few operands in form")
    elif max is not None and length > max:
        raise SchemeError("too many operands in form")

def check_formals(formals):
    """Check that FORMALS is a valid parameter list, a Scheme list of symbols
    in which each symbol is distinct.

    >>> check_formals(read_line("(a b c)"))
    """
    "*** YOUR CODE HERE ***"

##################
# Tail Recursion #
##################

def scheme_optimized_eval(expr, env):
    """Evaluate Scheme expression EXPR in environment ENV."""
    while True:
        if expr is None:
            raise SchemeError("Cannot evaluate an undefined expression.")

        # Evaluate Atoms
        if scheme_symbolp(expr):
            return env.lookup(expr)
        elif scheme_atomp(expr):
            return expr

        # All non-atomic expressions are lists.
        if not scheme_listp(expr):
            raise SchemeError("malformed list: {0}".format(str(expr)))
        first, rest = expr.first, expr.second

        # Evaluate Combinations
        if first in LOGIC_FORMS:
            "*** YOUR CODE HERE ***"
        elif first == "lambda":
            return do_lambda_form(rest, env)
        elif first == "mu":
            return do_mu_form(rest)
        elif first == "define":
            return do_define_form(rest, env)
        elif first == "quote":
            return do_quote_form(rest)
        elif first == "let":
            "*** YOUR CODE HERE ***"
        else:
            "*** YOUR CODE HERE ***"

################################################################
# Uncomment the following line to apply tail call optimization #
################################################################
# scheme_eval = scheme_optimized_eval


################
# Input/Output #
################

def read_eval_print_loop(next_line, env):
    """Read and evaluate input until an end of file or keyboard interrupt."""
    while True:
        try:
            src = next_line()
            while src.more_on_line:
                expression = scheme_read(src)
                result = scheme_eval(expression, env)
                if result is not None:
                    print(result)
        except (SchemeError, SyntaxError, ValueError) as err:
            print("Error:", err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc.
            return

def scheme_load(sym, env):
    """Load Scheme source file named SYM in environment ENV."""
    check_type(sym, scheme_symbolp, 0, "load")
    with scheme_open(sym) as infile:
        lines = infile.readlines()
    def next_line():
        return buffer_lines(lines)
    read_eval_print_loop(next_line, env.global_frame())

def scheme_open(filename):
    """If either FILENAME or FILENAME.scm is the name of a valid file,
    return a Python file opened to it. Otherwise, raise an error."""
    try:
        return open(filename)
    except IOError as exc:
        if filename.endswith('.scm'):
            raise SchemeError(str(exc))
    try:
        return open(filename + '.scm')
    except IOError as exc:
        raise SchemeError(str(exc))

def create_global_frame():
    """Initialize and return a single-frame environment with built-in names."""
    env = Frame(None)
    env.define("eval", PrimitiveProcedure(scheme_eval, True))
    env.define("apply", PrimitiveProcedure(scheme_apply, True))
    env.define("load", PrimitiveProcedure(scheme_load, True))
    add_primitives(env)
    return env

@main
def run(*argv):
    next_line = buffer_input
    if argv:
        try:
            filename = argv[0]
            input_file = open(argv[0])
            lines = input_file.readlines()
            def next_line():
                return buffer_lines(lines)
        except IOError as err:
            print(err)
            sys.exit(1)
    read_eval_print_loop(next_line, create_global_frame())
