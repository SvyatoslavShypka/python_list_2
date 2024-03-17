import fileinput


def process_all_lines(lines):
    print(lines)


if __name__ == '__main__':
    for fileinput_line in fileinput.input():
        fileinput_line = fileinput_line.rstrip().lstrip('\ufeff')
        if 'Exit' == fileinput_line.rstrip():
            break
        process_all_lines(fileinput_line)
