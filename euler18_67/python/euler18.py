__author__ = 'Reijer'

def loadtriangle():
    infile = open('p067_triangle.txt', 'r')
    return [[int(j) for j in i.split()] for i in infile]

def sumlist(n, m):
    for i in range(len(m)):
        if i == 0:
            totals = [n[0] + m[0]]
        elif i == len(n):
            return totals + [n[-1] + m[-1]]
        else:
            totals.append(max(n[i-1], n[i]) + m[i])

def main():
    triangle = loadtriangle()
    totals = sumlist(triangle[0], triangle[1])
    for i in range(2, len(triangle)):
        totals = sumlist(totals, triangle[i])
    print max(totals)
# van 2 de hoogste bij de waarde erboven op tellen is waarschijnlijk nog effiecenter

if __name__ == '__main__':
    main()