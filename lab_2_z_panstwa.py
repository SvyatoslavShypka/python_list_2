import sys
import fileinput


def wierszy_code(lines, panstwo):
    result = []
    for line in lines:
        line = line.rstrip().lstrip('\ufeff')
        data = line.split()
        if len(data) < 8:
            raise RuntimeError("Nieprawidlowe dane")
        if data[0].endswith(panstwo):
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
    panstwo = sys.argv[1]
    processed_output = wierszy_code(lines, panstwo)
    # Złączamy w jeden String
    processed_text = '\n'.join(processed_output)
    # Wyprowadzamy na stdout
    sys.stdout.buffer.write(processed_text.encode())


if __name__ == '__main__':
    if len(sys.argv) < 1:
        raise RuntimeError("Brak danych")
    process_code()
