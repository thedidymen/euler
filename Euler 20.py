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

def som():
    x = str(fact(100))
    print x
    som = 0
    for i in range(len(x)):
        som += int(x[i])
    # print j[i], som
    print som

if __name__ == '__main__':
    som()
