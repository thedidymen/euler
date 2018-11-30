
"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""


def prevlexper(l):
	# for index in range(len(l)-1):
	# 	if l[index] > l[index+1]:
	# 		prefix = l[:index-1]
	# 		pivot = l[index]
	# 		suffix = l[:index-1:-1]	
	# 		for indexswap in range(len(suffix)):
	# 			if pivot > suffix[indexswap]:
	# 				pivot, suffix[indexswap] = suffix[indexswap], pivot
	# 				return prefix + [pivot] + suffix
	# 	if index == len(l):
	# 		return l[::-1]
	for index in range(len(l)-2, -1, -1):
		# one number is always an increasing trend
		if l[index] > l[index+1]:
			# find index with the first decrease trend
			prefix = l[:index]
			pivot = l[index]
			suffix = l[:index:-1]
			for indexswap in range(len(suffix)):
				if suffix[indexswap] < pivot:
					#swap the first decrease, pivot, with the first number thats higher than pivot
					pivot, suffix[indexswap] = suffix[indexswap], pivot
					return prefix + [pivot] + suffix
		if index == 0:
			# if index reaches 0, current l is higest permutations (next permutation is the lowest)
			return l[::-1]


def nextlexper(l):
	for index in range(len(l)-2, -1, -1):
		# one number is always an increasing trend
		if l[index] < l[index+1]:
			# find index with the first decrease trend
			prefix = l[:index]
			pivot = l[index]
			suffix = l[:index:-1]
			for indexswap in range(len(suffix)):
				if suffix[indexswap] > pivot:
					#swap the first decrease, pivot, with the first number thats higher than pivot
					pivot, suffix[indexswap] = suffix[indexswap], pivot
					return prefix + [pivot] + suffix
		if index == 0:
			# if index reaches 0, current l is higest permutations (next permutation is the lowest)
			return l[::-1]

def genlexper(l, reverse=False):
	if not reverse:
		current = nextlexper(l)
	else:
		current = prevlexper(l)
	yield current
	while current != l:
		if not reverse:
			current = nextlexper(current)
		else:
			current = prevlexper(current)

		yield current










if __name__ == '__main__':
	l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

	p = genlexper(l)
	# pr = prevlexper(l)

	# for i in range(999999):
	# 	if i == 999998:
	# 		print next(p)
	# 	next(p)

	n = next(p)

	for i in range(10):
		print n
		n = next(p)
		print prevlexper(n)
		print
	
	

