import sys
import fileinput


def is_code_200(line):
    data = line.split()
    # print(data)
    if len(data) < 8:
        raise RuntimeError("Nieprawidlowe dane")
    return data[len(data) - 2] == '302'


if __name__ == '__main__':
    if len(sys.argv) < 1:
        raise RuntimeError("Brak danych")
    count = 0
    processed_output = []
    for fileinput_line in fileinput.input():
        fileinput_line = fileinput_line.rstrip().lstrip('\ufeff')
        # print(fileinput_line)
        if 'Exit' == fileinput_line.rstrip():
            break
        if is_code_200(fileinput_line):
            count += 1
    processed_output.append(str(count))
    # Złączamy w jeden String
    processed_text = '\n'.join(processed_output)
    # Wyprowadzamy na stdout
    sys.stdout.buffer.write(processed_text.encode())
