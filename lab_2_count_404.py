import sys
import fileinput


def is_code_404(line):
    data = line.split()
    if len(data) < 10:
        raise RuntimeError("Nieprawidlowe dane")
    return data[8] == '404'


if __name__ == '__main__':
    if len(sys.argv) < 1:
        raise RuntimeError("Brak danych")
    count = 0
    processed_output = []
    for fileinput_line in fileinput.input():
        fileinput_line = fileinput_line.rstrip().lstrip('\ufeff')
        if is_code_404(fileinput_line):
            count += 1
        if 'Exit' == fileinput_line.rstrip():
            break
    processed_output.append(str(count))
    # Złączamy w jeden String
    processed_text = '\n'.join(processed_output)
    # Wyprowadzamy na stdout
    sys.stdout.buffer.write(processed_text.encode())
