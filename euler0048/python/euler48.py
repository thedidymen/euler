__author__ = 'Reijer'

def test():
    x = 0
    for i in range(1, 1001):
        x += i**i
        print i, x

if __name__ == '__main__':
    test()