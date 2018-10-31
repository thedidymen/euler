# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, ther are exactly 6 routes to the bottom right corner.
# How many such routes are there in a 20x20 grid?

def fact(n):
	f = 1
	for i in range(1, n+1):
		f *= i
	return f

def C(n, k):
	assert n > k
	assert k > 0
	return fact(n)/(fact(k)*fact(n-k))

if __name__ == '__main__':
	print C(40, 20)