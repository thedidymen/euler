
"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""


def prevlexper(l):
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


def nextlexper(l, reverse=False):
	for index in range(len(l)-2, -1, -1):
		if reverse:
			# next or previos permutations
			pivotpoint = l[index] < l[index+1]
		elif not reverse:
			pivotpoint = l[index] > l[index+1]
		else:
			raise error
		# one number is always an increasing trend
		if pivotpoint:
			# find index with the first decrease trend
			prefix = l[:index]
			pivot = l[index]
			suffix = l[:index:-1]
			for indexswap in range(len(suffix)):
				if reverse:
					# next or previos permutations
					swappoint = suffix[indexswap] > pivot
				elif not reverse:
					swappoint = suffix[indexswap] < pivot
				else:
					raise error
				if swappoint:
					#swap the first decrease, pivot, with the first number thats higher than pivot
					pivot, suffix[indexswap] = suffix[indexswap], pivot
					return prefix + [pivot] + suffix
		if index == 0:
			# if index reaches 0, current l is higest permutations (next permutation is the lowest)
			return l[::-1]

def genlexper(l, reverse=False):
	current = nextlexper(l, reverse=reverse)
	yield current

	while current != l:
		current = nextlexper(current, reverse=reverse)

		yield current










if __name__ == '__main__':
	# l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	l = [0,1,2,3]

	nextlex = genlexper(l)
	prevlex = genlexper(l, reverse=True)
	# # pr = prevlexper(l)

	# # for i in range(999999):
	# # 	if i == 999998:
	# # 		print next(p)
	# # 	next(p)

	# n = next(nextlex)
	# p = next(prevlex)


	# for i in range(24):
	# 	print n, p
	# 	n = next(nextlex)
	# 	p = next(prevlex)

	per4 = [p for p in nextlex]
	product, l = [], []

	print len(per4[0])
	print len(per4)


	for i in range(len(per4)):
		for n in range(len(per4[0])):
			l.append(per4[i][n])
		product.append(l)
	for j in product:
		print j
	
	

