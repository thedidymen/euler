
primes = [2,]

def isprime(n):
	if n > 1:
		for prime in primes:
			if n in primes:
				return True
			elif n % prime == 0:
				return False
		primes.append(n)
		return True
	else:
		return False

def nextprime():
	n = 1
	while True:
		n += 1
		if n in primes:
			yield n
		elif isprime(n):
			yield n



if __name__ == '__main__':
	n = 600851475143
	p = [i for i in range(-10, 100) if isprime(i)]
	print p
	gen = nextprime()
	for i in range(110):
		print next(gen)