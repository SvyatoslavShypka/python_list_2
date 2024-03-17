import sys
import fileinput


def najwiekszy_zasob(lines):
    max = 0
    link = ""
    for line in lines:
        data = line.split()
        if len(data) < 8:
            raise RuntimeError("Nieprawidlowe dane")
        indeks = len(data) - 1
        if data[indeks] == '-':
            continue
        bajty = int(data[indeks])
        if max < bajty:
            max = bajty
            link = data[len(data) - 4]
    return link + " : " + str(max)


if __name__ == '__main__':
    if len(sys.argv) < 1:
        raise RuntimeError("Brak danych")
    processed_output = []
    processed_output = [najwiekszy_zasob(fileinput.input())]
     # Złączamy w jeden String
    processed_text = '\n'.join(processed_output)
    # Wyprowadzamy na stdout
    sys.stdout.buffer.write(processed_text.encode())
