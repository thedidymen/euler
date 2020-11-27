__author__ = 'Reijer'

memo = [1,1]

def fact(n):
    if n == 1 or n == 0:
        return 1
    if len(memo)>n:
        return memo[n]
    else:
        memo.append(n*fact(n-1))
    return memo[n]

def test():
    l =[]
    for n in range(7*fact(9)):
        s = str(n)
        m = 0
        for i in range(len(s)):
            m += fact(int(s[i]))
        if m == n:
            print n
            l.append(n)

if __name__ == '__main__':
    test()
