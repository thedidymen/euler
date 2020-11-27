__author__ = 'Reijer'

def test():
    d={
        1 : "one",
        2 : "two",
        3 : "three",
        4 : "four",
        5 : "five",
        6 : "six",
        7 : "seven",
        8 : "eight",
        9 : "nine",
        10 : "ten",
        11 : "eleven",
        12 : "twelve",
        13 : "thirteen",
        14 : "fourteen",
        15 : "fifteen",
        16 : "sixteen",
        17 : "seventeen",
        18 : "eighteen",
        19 : "nineteen",
        20 : "twenty",
        30 : "thirty",
        40 : "forty",
        50 : "fifty",
        60 : "sixty",
        70 : "seventy",
        80 : "eighty",
        90 : "ninety",
        100: "hundred",
        1000: "thousand"
    }
    length = 0
    for i in range(1, 1001):
        length += lettercount(i, d)
    print length

    # length10 = 0
    # for i in range(1, 10):
    #     length10 += len(d.get(i))
    # length20 = 0
    # for i in range(10, 20):
    #     length20 += len(d.get(i))
    # length100 = length10 + length20
    # for i in range(20, 100, 10):
    #     length100 += 10 * len(d.get(i)) + length10
    # length100a = length10
    # for i in range(10, 100, 10):
    #     length100a += 10 * len(d.get(i)) + length10
    # length1000 = length100
    # for i in range(1, 10, 1):
    #     length1000 += 100 * (len(d.get(i))+ len(d.get(100))+ len("and")) + length100a
    #     print i, length1000
    # length1000 -= 24
    # print length1000

def lettercount(number, d):
    strnumber = str(number)
    if len(str(number)) == 4:
        return len(d.get(1000)) + lettercount(int(strnumber[1:]),d) + lettercount(int(strnumber[0:1]),d)
    if len(str(number)) == 3:
        if number%100==0:
            return len(d.get(int(strnumber[0:1]))) + len(d.get(100))
        else:
            return len(d.get(int(strnumber[0:1]))) + 3 + len(d.get(100)) + lettercount(int(strnumber[1:]),d)
    if len(str(number)) == 2:
        if number <= 20:
            return len(d.get(number))
        elif number%10==0:
            return len(d.get(10*(int(strnumber[0:1]))))
        else:
            return len(d.get(10*(int(strnumber[0:1])))) + lettercount(int(strnumber[1:]),d)
    if len(str(number)) == 1:
        if number == 0:
            return 0
        else:
            return len(d.get(number))


if __name__ == '__main__':
    test()
