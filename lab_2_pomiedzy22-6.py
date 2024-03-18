import sys
import fileinput


def wierszy(lines):
    result = []
    for line in lines:
        line = line.rstrip().lstrip('\ufeff')
        data = line.split()
        if len(data) < 8:
            raise RuntimeError("Nieprawidlowe dane")
        indeks = len(data) - 2
        if data[indeks] == '200':
            godzina = int(data[3][-8: -6])
            # pomiedzy 22 a 6 godzina
            if 22 <= godzina or godzina < 6:
                result.append(line)
    return result


if __name__ == '__main__':
    if len(sys.argv) < 1:
        raise RuntimeError("Brak danych")
    processed_output = wierszy(fileinput.input())
    # Złączamy w jeden String
    processed_text = '\n'.join(processed_output)
    # Wyprowadzamy na stdout
    sys.stdout.buffer.write(processed_text.encode())
