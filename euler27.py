
from functools import reduce
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
			for prime in self.primes:
				if n in self.primes:
					return True
				elif prime >= int(math.sqrt(n)+1):
					self.primes.append(n)
					return True
				elif n % prime == 0:
					return False
		else:
			return False

	def nextprime(self, n=1):
		while True:
			n += 1
			if n > len(self.primes):
				currentnumber = self.primes[-1]+1
				while not self.isprime(currentnumber):
					currentnumber += 1
			yield self.primes[n-2]

	def giveprimes(self, n):
		"""returns list up to and including n"""
		if n > self.primes[-1]:
			for current in range(self.primes[-1], n+1):
				self.isprime(current)
		return [prime for prime in self.primes if prime <= n]

	def trialdivision(self, n):
		assert(n >= 2)
		if self.isprime(n):
			return [n]
		primelist = self.giveprimes(int(math.sqrt(n)+1))
		for prime in primelist:
			if n % prime == 0:
				return [prime] + self.trialdivision(n=n/prime)

	def divisors(self, n):
		listofprimes = self.trialdivision(n)
		factors = {prime:listofprimes.count(prime)+1 for prime in listofprimes}
		return reduce(lambda x, y: x*y, factors.values())


if __name__ == '__main__':
	p = prime()
	primebelowm = p.giveprimes(1000)
	products = [0,0,0,0]
	for a in range(-1001, 1001):
		for b in primebelowm:
		# for b in range(-1001, 1001):
			counter = 0
			while p.isprime(counter**2+counter*a+b):
				counter += 1
			if counter > products[3]:
				products = [a, b, a*b, counter]
				print products

	print products
