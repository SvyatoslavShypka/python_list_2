import fileinput


def print_all_lines(lines):
    print(lines)


if __name__ == '__main__':
    for fileinput_line in fileinput.input():
        fileinput_line = fileinput_line.rstrip().lstrip('\ufeff')
        if 'Exit' == fileinput_line.rstrip():
            break
        print(fileinput_line)
