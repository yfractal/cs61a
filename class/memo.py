def memo(f):
	cache = {}
	def memoized(n):
		print("in memoized")
		print(n)
		print(cache)
		if n not in cache:
			# caculate nth fib
			cache[n] = f(n)
		return cache[n]
	return memoized

@memo 
def fib(n):
	if n == 1:
		return 0
	if n == 2:
		return 1
	return fib(n-2) + fib(n-1)

# f = fib(10)
# print(f)