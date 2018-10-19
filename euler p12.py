__author__ = 'Reijer'

memo = [1]

def factor(n):
    return [i for i in range(1, n+1) if n % i == 0]

def triangle(n):
    if n == 1:
        return 1
    if len(memo) > n-1:
        return memo[n-1]
    next = n + triangle(n-1)
    if next not in memo:
        memo.append(next)
    return memo[-1]

def main():
    # print len(factor(12))
    fact, i = [], 0
    while len(fact) < 100:
        i += 1
        tri = triangle(i)
        # print i, tri
        fact = factor(tri)
        print i, tri, len(fact), fact
    print i





if __name__ == '__main__':
    main()