"""
Project Euler
Problem 29 - Distinct powers 

Consider all integer combinations of a^b for 2 <= a <= 5 and 2 <= b <= 5:

2^2=4, 2^3=8, 2^4=16, 2^5=32
3^2=9, 3^3=27, 3^4=81, 3^5=243
4^2=16, 4^3=64, 4^4=256, 4^5=1024
5^2=25, 5^3=125, 5^4=625, 5^5=3125

if they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:
	4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

How many distinct terms are in the sequence generated by a^b for 2 <= a <= 100 and 2 <= a <= 100?
"""

"""
Solutions thoughts. Distinct terms will be 99*99 - doulbe entries. 4^2 == 2^4 ==> (2^2)^2 == 2^4. 
However some of the 4 based powers should be included. 4^50 == 2^2^50 = 2^100. 2^100 is the last to be included in the double range.
"""


# def name(a, b):
# 	l = []
# 	for base in range(2, a+1):
# 		for power in range(2, b+1):
# 			l.append(base**power)
# 	l.sort()
# 	return l

if __name__ == '__main__':
	l = []
	for i in range(2, 101):
		for j in range(2, 101):
			p = i ** j
			if p not in l:
				l.append(p)
	print len(l)




