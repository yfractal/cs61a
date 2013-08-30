(
	(
	(lambda 
					(f) 
					(lambda (x) (f f x))
					)
	
  (
  	lambda (f k) 
  			(if (zero? k) 
  						1 (* k (f f (- k 1)))
  						)
  			)
  ) 
		5
		)

(eval (cons 
				'car '(
					'(1 2)
							)
				)
	)