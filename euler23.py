

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


def factors(n):
    """Gives list of proper divisors, inclucding n"""
    counter = 1
    divisors = []
    while counter < int(n**0.5)+1:
        if n%counter == 0:
            divisors.append(counter)
            if counter != n/counter:    #remove "and test != 1" if you want to include n itself
            	# prevents entering the same number twice
            	divisors.append(n/counter)
        counter += 1
    divisors.sort()
    return divisors

def sumofdivisors(list):
	return sum(list[0:-1])

def abundantnumbers(n):
	return [i  for i in range(n+1) if sumofdivisors(factors(i)) > i]


if __name__ == '__main__':
	n = 28123
	listofabundantnumbers = abundantnumbers(n)
	l = range(n)
	for i in listofabundantnumbers:
		print listofabundantnumbers.index(i), "/", len(listofabundantnumbers)
		print "integers left:", len(l)
		for j in listofabundantnumbers:
			s = i + j
			if s < n:
				if s in l:
					l.remove(s)
	print l, sum(l)


	
				
