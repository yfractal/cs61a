; # 1 The Scheme Interpreter
; # Everything is an expression.

; # ’a ; this is a symbol

; # ’a, you get a. This is because when you
; # use the single quote, you’re telling Scheme not to follow the normal rules of evaluation
; # and just have the symbol return as itself.

; STk> (define a 1)
; a
; STk> a
; 1
; STk> (define b a)
; b
; STk> (define c 'a)
; c
; STk> c
; a
; STk> 

; 3 Evaluating Function Calls and Special Forms
; 3.1 Functions
;  +, -, *, /
;  eq?, =, >, >=, <, <=
; 3.2 Questions
; STk> (+ 1)
; 1
; STk> (* 3)
; 3
; STk> (+ (* 3 3) ( * 4 4))
; 25
; STk> (define a (define b 3))
; a
; STk> a
; b
; STk> b
; 3
; STk> 'a
; a
; STk> 

; 3.3 Special Forms
; STk> (and 1 2 3)
; 3
; STk> (or 1 2 3)
; 1
; STk> (or #t (/ 1 0))
; #t
; STk> (and #f (/1 0))
; #f
; STk> (not 3)
; #f
; STk> (not #t)
; #f

; 3.4 Questions
; STk> (if (or #t (/ 1 0)) 1 (/ 1 0))
; 1
; STk> (if (> 4 3) (+ 1 2 3 4) (+ 3 4 (* 3 2)))
; 10
; STk> ((if (< 4 3) + -) 4 100)
; -96

; 4 Lambdas, Environments and Deﬁning Functions
; Note that <EXPR> is
; not evaluated until the lambda value is called.

; When you do (define (<FUNCTIONNAME> <PARAMETERS>) <EXPR>), Scheme will
; automatically transform it to (define <FUNCTIONNAME> (lambda (<PARAMETERS>)
; <EXPR>) for you.

; lambda- let
; (let ( 
; 	(<SYMBOL1> <EXPR1>)
; 		...
; 	(<SYMBOLN> <EXPRN>) 
; 	)
; <BODY> 
; )
; ( (lambda (<SYMBOL1> ... <SYMBOLN>) <BODY>) <EXPR1> ... <EXPRN>)
; You’ll notice that what let does then is bind symbols to expressions.

; ............
(define (sin x)
	(if (< x 0.000001)
		x
		(let ((recursive-step (sin (/ x 3))) ) ;let here
				 (- 
				 	(* 3 recursive-step) (* 4 (expt recursive-step 3))
				 	)
			)
		)
	)
; 4.1 Questions
; 1. Write a function that calculates factorial. (Note how you haven’t been told any methods for iteration.)
 (define (factorial x)
 	(if (= x 1)
         x
		(* 
			x (factorial (- x 1)))
		)
 	)

 (define (fib n)
	(if (< n 2)
		1
		(+
			(fib (- n 1)) (fib (- n 2))
			)
		)
	)

; 5 Pairs and Lists
; constructor cons which takes two arguments
; car and
; cdr
; car (short for "Contents of the Address part of Register number"),
; cdr ("Contents of the Decrement part of Register number"),

; STk> (define a (cons 1 2))
; a
; STk> a
; (1 . 2)
; ; separated by a period.
; STk> (car a)
; 1
; STk> (cdr a)
; 2

; the empty  list whose literal is ’(), also known as nil
; STk> ’()
; ()
; STk> nil
; ()
; STk> (cons 1 (cons 2 nil))
; (1 2)
; STk> (cons 1 (cons 2 (cons 3 nil)))
; (1 2 3)


; hat is because when a dot is followed by the left parenthesis, the dot and the left parenthesis are deleted; when a left parenthesis is deleted, its
; matching right parenthesis is deleted also.

; null?

;  When you use the single quote,
; you’re telling Scheme not to evaluate the list, but instead keep it as just a list.
; This is why Scheme is cool. It can be deﬁned within itself.
(define (map fn lst)
	(if (null? lst)
		null
		(cons (
			(fn (car last))
			(map fn (cdr last)))
		)
	)
)

(define (reduce fn s lst)
	(if (null? lst)
		s
		fn( 
			(car lst) (reduce(fn s lst))
			)
		)
	)

(define (make-btree entry left right)
	(cons 
		entry
		(cons left right)
		)

	(define (entry tree)
		(car tree)
		)
	(define (left tree)
		(car (cdr tree))
		)
	(define (right tree)
		(cdr (cdr tree))
		)
	)

(define (btree-sum tree)
	(if (null? tree)
		0
		(+ 
			entry(tree) btree-sum(left(tree)) btree-sum(right(tree))
			)
		)
	)