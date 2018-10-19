__author__ = 'Reijer'
import math

def prime(n):
    return bool(n%2) and all(n%d for d in range(3, int(math.sqrt(n))+1, 2))

def sum():
    som = 2
    for n in range(3, 2000000, 2):
        if prime(n) == True:
            som += n
    print som

if __name__ == '__main__':
    sum()