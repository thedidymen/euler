
# class Spiral(object):
# 	"""docstring for Spiral"""
# 	def __init__(self, n):
# 		super(Spiral, self).__init__()
# 		self.matrix = self.buildspiral(n)
# 	def buildspiral(self, n):
# 		for number in range(n):

def quadratic(n, a, b, c):
	return a*n**2 + b*n + c




if __name__ == '__main__':
	base = 1001
	a = 4
	ball = [-2, 0, 2, 4]
	c = 1
	sumup = 1
	for n in range(1, int(base/2)+1):
		for b in ball:
			q = quadratic(n=n, a=a, b=b, c=c)
			sumup += q
	print sumup