(define (reduce fn s star)
	(if (null? s) start
		(reduce fn
			(cdr s)
			(fn start (car s))
			)
		)
	)

(reduce 
	(
		lambda(x y)
		(cons y x) 
	)
		'(3 4 5)
		'(2)
	)
)
