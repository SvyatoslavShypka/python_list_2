import sys


def wierszy_code(lines, code):
    result = []
    for line in lines:
        line = line.rstrip().lstrip('\ufeff')
        # print(line)
        data = line.split()
        # print(data)
        if len(data) < 8:
            raise RuntimeError("Nieprawidlowe dane")
        indeks = len(data) - 2
        if data[indeks] == code:
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
    code = sys.argv[1]
    processed_output = wierszy_code(lines, code)
    # Złączamy w jeden String
    processed_text = '\n'.join(processed_output)
    # Wyprowadzamy na stdout
    sys.stdout.buffer.write(processed_text.encode())


if __name__ == '__main__':
    if len(sys.argv) < 1:
        raise RuntimeError("Brak danych")
    process_code()
