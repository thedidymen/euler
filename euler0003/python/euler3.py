import math

class prime(object):
	"""docstring for prime"""
	def __init__(self, primes=[2, ]):
		super(prime, self).__init__()
		self.primes = primes

	def currentprimes(self):
		return self.primes

	def isprime(self, n):
		if n == 2:
			return True
		elif n > 1:
			nmax = int(math.sqrt(n)+1)
			for prime in self.primes:
				if prime >= nmax:
					self.primes.append(n)
					return True
				elif n in self.primes:
					return True
				elif n % prime == 0:
					return False
		else:
			return False

	def nextprime(self):
		n = 1
		while True:
			n += 2
			if n in self.primes:
				yield n
			elif self.isprime(n):
				yield n



if __name__ == '__main__':
	n = 600851475143
	nmax = int(math.sqrt(n)+1)
	print nmax
	p = prime()
	gen = p.nextprime()
	nextgen = next(gen)
	l = []
	while nextgen < nmax:
		nextgen = next(gen)
		if n % nextgen == 0:
			print nextgen
			l.append(nextgen)




