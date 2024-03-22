import sys


def count_code(lines, code):
    count = 0
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
            count += 1
            result.append(line)
    return count


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
    processed_output = str(count_code(lines, code))
    # Wyprowadzamy na stdout
    sys.stdout.buffer.write(processed_output.encode())


if __name__ == '__main__':
    if len(sys.argv) < 1:
        raise RuntimeError("Brak danych")
    process_code()


# if __name__ == '__main__':
#     if len(sys.argv) < 1:
#         raise RuntimeError("Brak danych")
#     count = 0
#     processed_output = []
#     for fileinput_line in fileinput.input():
#         fileinput_line = fileinput_line.rstrip().lstrip('\ufeff')
#         # print(fileinput_line)
#         if 'Exit' == fileinput_line.rstrip():
#             break
#         if is_code_200(fileinput_line):
#             count += 1
#     processed_output.append(str(count))
#     # Złączamy w jeden String
#     processed_text = '\n'.join(processed_output)
#     # Wyprowadzamy na stdout
#     sys.stdout.buffer.write(processed_text.encode())
