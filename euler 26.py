__author__ = 'Reijer'


def ld(n, ans = "0.", remainder = -1, multi = []):
    if remainder == 0:
        return str(ans)
    elif remainder*10 in multi:
        index = multi.index(remainder)
        return ans[:index] + "(" + ans[index:] + ")"
    else:
        factor = (10 ^ (len(str(n)))) / n
        remainder = n % factor
        ans += str(factor)
        multi.append(factor*n)
        print n, ans, remainder, multi, factor
        return ld(n, ans, remainder, multi)

def main():
    for i in range(2, 1001):
        print ld(i)

if __name__ == '__main__':
    main()