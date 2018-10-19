__author__ = 'Reijer'

def loadnames(file):
    namefile = open(file)
    return sorted([name.strip("\"") for line in namefile for name in line.split(",")])

def main():
    namelist = loadnames("p022_names.txt")
    alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print namelist
    counter,total  = 0, 0
    for item in namelist:
        counter += 1
        total += counter*reduce(lambda x,y: x + y, (alphabet.index(i) for i in item))
    print total

if __name__ == '__main__':
    main()