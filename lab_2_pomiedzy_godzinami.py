import sys


def wierszy_godziny(lines, godzina_od, godzina_do):
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
            if godzina_od <= godzina or godzina < godzina_do:
                result.append(line)
    return result


def input_data():
    result_data = []
    while True:
        try:
            result_data.append(input())
        except:
            break
    return result_data


def process_code():
    lines = input_data()
    godzina_od = int(sys.argv[1])
    godzina_do = int(sys.argv[2])
    processed_output = wierszy_godziny(lines, godzina_od, godzina_do)
    # Złączamy w jeden String
    processed_text = '\n'.join(processed_output)
    # Wyprowadzamy na stdout
    sys.stdout.buffer.write(processed_text.encode())


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise RuntimeError("Brak danych")
    process_code()
