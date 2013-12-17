"""
These are all the functions I use repeatedly. But I am too lazy to rewrite things. So I created a custom module out of them.
"""

def fibonacci(n):
	"""fibonacci(n) -> Return the nth Fibonacci number"""
	assert n > 0
	if n <= 317:
		f2, f1 = 1, 1
		for x in xrange(2, n):
			f2, f1 = f2 + f1, f2
		return f2
	else:
		ans = [[1, 0], [0, 1]]
		fib = [[1, 1], [1, 0]]
		while n != 0:
			if n%2 == 1:
				ans = [[ans[0][0]*fib[0][0]+ans[0][1]*fib[1][0], ans[0][0]*fib[0][1]+ans[0][1]*fib[1][1]], [ans[1][0]*fib[0][0]+ans[1][1]*fib[1][0], ans[1][0]*fib[0][1]+ans[1][1]*fib[1][1]]]
			fib = [[fib[0][0]**2+fib[0][1]*fib[1][0], fib[0][0]*fib[0][1]+fib[0][1]*fib[1][1]], [fib[1][0]*fib[0][0]+fib[1][1]*fib[1][0], fib[1][0]*fib[0][1]+fib[1][1]**2]]
			n /= 2
		return ans[0][1]

def compare(word1, word2):
	for i, j in zip(word1, word2):
		if i != j:
			return cmp(i, j)
	return cmp(len(word1), len(word2))

def wordSort(listOfNames):
	"""Sort a list of words Alphabetically"""
	listOfNames.sort(compare)

