__author__ = 'Reijer'

def construct():
    matrix = open("matrix.txt", "r")
    thematrix = []
    for line in matrix:
        row = [int(digits) for digits in line.split()]
        thematrix.append(row)
    return thematrix

# def diaclock(thematrix, col, row, maxi):
#     current = 1
#     for i in range(4):
#         current *= thematrix[row+i][col+i]
#     if current > maxi:
#         return maxi
#     else:
#         return current
#
# def diacounterclock(thematrix, col, row, maxi):
#     current = 1
#     for i in range(4):
#         current *= thematrix[row-i][col-i]
#     if current > maxi:
#         return maxi
#     else:
#         return current
#
# def vertical(thematrix, col, row, maxi):
#     current = 1
#     for i in range(4):
#         current *= thematrix[row+i][col]
#     if current > maxi:
#         return maxi
#     else:
#         return current
#
# def horizontal(thematrix, col, row, maxi):
#     current = 1
#     for i in range(4):
#         current *= thematrix[row][col+i]
#     if current > maxi:
#         return maxi
#     else:
#         return current
#

def main():
    maxi = 1
    thematrix = construct()
    for row in range(16):
        # only need to check until row 16: 16+4  =20
        for col in range(20):
            horizontal, diaclock, diacounterclock, vertical = 1, 1, 1, 1 #resetting values
            for i in range(4):
                if col <= 16:
                    # making sure we don exceed the table
                    horizontal *= thematrix[row][col+i]
                    diaclock *= thematrix[row+i][col+i]
                if col >= 4:
                    # making sure we don exceed the table
                    diacounterclock *= thematrix[row+i][col-i]
                    vertical *= thematrix[row+i][col]
            maxi = max(horizontal, diaclock, diacounterclock, vertical, maxi)
    print maxi


if __name__ == '__main__':
    main()