import sys
import fileinput


def sites(lines):
    data = lines.split()
    if len(data) < 10:
        raise RuntimeError("Nieprawidlowe dane")
    return data[0]


if __name__ == '__main__':
    if len(sys.argv) < 1:
        raise RuntimeError("Brak danych")
    processed_output = []
    for fileinput_line in fileinput.input():
        fileinput_line = fileinput_line.rstrip().lstrip('\ufeff')
        if 'Exit' == fileinput_line.rstrip():
            break
        processed_output.append(sites(fileinput_line))
    # Złączamy w jeden String
    processed_text = '\n'.join(processed_output)
    # Wyprowadzamy na stdout
    sys.stdout.buffer.write(processed_text.encode())
