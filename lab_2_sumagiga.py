import sys
import fileinput


def suma(lines):
    sum = 0
    for line in lines:
        data = line.split()
        if len(data) < 8:
            raise RuntimeError("Nieprawidlowe dane")
        indeks = len(data) - 1
        if data[indeks] != '-':
            sum += int(data[indeks])

    return str(sum/(1024*1024*1024))


if __name__ == '__main__':
    if len(sys.argv) < 1:
        raise RuntimeError("Brak danych")
    processed_output = []
    processed_output = [suma(fileinput.input())]
     # Złączamy w jeden String
    processed_text = '\n'.join(processed_output)
    # Wyprowadzamy na stdout
    sys.stdout.buffer.write(processed_text.encode())
