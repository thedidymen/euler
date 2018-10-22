import math




class prime(object):
	"""docstring for prime"""
	def __init__(self, primes=[2, ]):
		super(prime, self).__init__()
		self.primes = primes

	def currentprimes(self):
		return self.primes

	def isprime(self, n):
		if n > 1:
			for prime in self.primes:
				if n in self.primes:
					return True
				elif n % prime == 0:
					return False
			self.primes.append(n)
			return True
		else:
			return False

	def nextprime(self):
		n = 1
		while True:
			n += 1
			if n in self.primes:
				yield n
			elif self.isprime(n):
				yield n


if __name__ == '__main__':
	p = prime()
	listofprimes = [i for i in range(-10, 100) if p.isprime(i)]
	print listofprimes
	print p.currentprimes()
	gen = p.nextprime()
	for i in range(110):
		print next(gen)
	print p.currentprimes()


