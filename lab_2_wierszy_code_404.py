import sys
import fileinput


def wierszy_code(lines):
    result = []
    for line in lines:
        line = line.rstrip().lstrip('\ufeff')
        data = line.split()
        if len(data) < 8:
            raise RuntimeError("Nieprawidlowe dane")
        indeks = len(data) - 2
        if data[indeks] == '404':
            result.append(line)
    return result


if __name__ == '__main__':
    if len(sys.argv) < 1:
        raise RuntimeError("Brak danych")
    processed_output = wierszy_code(fileinput.input())
    # Złączamy w jeden String
    processed_text = '\n'.join(processed_output)
    # Wyprowadzamy na stdout
    sys.stdout.buffer.write(processed_text.encode())
