import sys
import fileinput
import re


def stosunek_grafiki(lines):
    grafika = 0
    wszystkie = 0
    for line in lines:
        line = line.rstrip().lstrip('\ufeff')
        data = line.split()
        if len(data) < 8:
            raise RuntimeError("Nieprawidlowe dane")
        indeks = len(data) - 2
        if data[indeks] == '200':
            wszystkie += 1
            check = re.search("\\.(gif)|(jpe*g)|(xbm)", line)
            if check:
                grafika += 1
    stosunek_procent = round(grafika / wszystkie * 100, 2)
    return str(stosunek_procent) + "%"


if __name__ == '__main__':
    # cat NASA | python lab_2_stosunek_grafiki.py
    # {'302'-Redirected, '200'-Ok, '404'-Not found, '304'-Not modified, '400'-Bad request}
    if len(sys.argv) < 1:
        raise RuntimeError("Brak danych")
    processed_output = []
    processed_output = [stosunek_grafiki(fileinput.input())]
     # Złączamy w jeden String
    processed_text = '\n'.join(processed_output)
    # Wyprowadzamy na stdout
    sys.stdout.buffer.write(processed_text.encode())
