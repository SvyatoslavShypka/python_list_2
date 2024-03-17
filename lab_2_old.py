import sys
dane = sys.argv[1]
f = open(dane, "r")
while True:
    line = f.readline()
    if not line:
        break
    print(line)


# if __name__ == '__main__':
