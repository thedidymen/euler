def trianglenumber(n):
	return sum(range(n+1))

def factors(n):
    """Gives list of proper divisors, excludes n"""
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



if __name__ == '__main__':
	n = 1
	triangle = trianglenumber(n)
	l = factors(triangle)
	while len(l) < 500:
		n += 1
		triangle = trianglenumber(n)
		l = factors(triangle)
	print n, triangle, l

