import sys


def code_count(file_name, code):
    count = 0
    with open(file_name, 'r') as a:
        data = []
        for line in a:
            data = line.split()
            if data[8] == '200':
                count += 1
                print('code= ' + data[8], end='\n')
    print(count)
    return count


if __name__ == '__main__':
    code_count(sys.argv[1], sys.argv[2])
