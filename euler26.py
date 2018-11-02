


def reciprocalcycles(d, n=1):
	""""""
	if n % d == 0:
		print n, d, n%d
		return [n / d]
	if n / d == 0:
		print n, d, n/d
		return [0] + reciprocalcycles(n=n*10, d=d)
	if n / d > 0:
		print n, d, n/d
		return [n / d] + reciprocalcycles(n=n, d=n%d)




if __name__ == '__main__':
	for i in range(2, 10):
		print i
		print reciprocalcycles(d=i)
		print
	