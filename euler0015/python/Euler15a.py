__author__ = 'Reijer'

def fact(n):
    """

    :param n:
    :return:
    """
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

def main():
    print (fact(20)/(fact(2)*fact(18)))




if __name__ == '__main__':
    main()