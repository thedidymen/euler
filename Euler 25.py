__author__ = 'Reijer'

def fib(f1, f2):
    return f1 + f2

def test ():
    f1 = 1
    f2 = 1
    counter = 2
    while len(str(f2)) != 1000:
        # print f1, f2, counter
        f3 = f1 + f2
        counter += 1
        f1 = f2
        f2 = f3
    print counter

if __name__ == '__main__':
    test()
