

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


def test():
	print "check function .isprime(n)"
	p = prime()
	listofprimes = [i for i in range(-10, 100) if p.isprime(i)]
	print listofprimes
	print
	print "check currentprimes"
	g = prime()
	print "while empty"
	print p.currentprimes()
	print "fill with primes upto 20"
	listofprimes = [i for i in range(20) if p.isprime(i)]
	print p.currentprimes()
	print
	print "generator nextprime"
	h = prime()
	print "give the first 10 primenumbers"
	for i in range(10):
		print next(p.nextprime())



if __name__ == '__main__':
	# test()
	# p = prime()
	# for i in range(1, 101):
	# 	print i, p.giveprimes(i)

	# g = prime()
	# gen = g.nextprime()
	# for i in range(1, 101):
	# 	print i, next(gen)

	# gen = g.nextprime(10)
	# for i in range(1, 101):
	# 	print i+10, next(gen)

	p = prime()
	for n in range(2, 100):
		# print n, p.trialdivision(n)
		print n, p.giveprimes(n)




