def collatz(n):
    """Gives Collatz sequence for a given n"""
    if n == 1:
        return []
    elif n % 2 == 0:
        return [n/2] + collatz(n/2)
    else:
        return [3*n+1] + collatz(3*n+1)


def test():
    """gives back longest Collatz sequence beneath 1000000"""
    l = [0,0]
    for n in range(1, 1000000):
        x = collatz(n)
        if len(x)> l[0]:
            l = [len(x), n]
    print l, collatz(l[1])

if __name__ == '__main__':
    test()