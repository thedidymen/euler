__author__ = 'Reijer'


def factors(n):
    """Gives list of proper divisors, excludes n"""
    test = 1
    l = []
    while test < int(n**0.5)+1:
        if n%test == 0:
            l.append(test)
            if test != n/test and test != 1:    #remove "and test != 1" if you want to include n itself
                l.append(n/test)
        test += 1
    l.sort()
    return l

def test():
    l = []
    for i in range(1, 10001):
        x = sum(factors(i))
        if i == sum(factors(x)) and i != x:
            l.append(x)
    l.sort()
    print l, sum(l)

if __name__ == '__main__':
    test()
