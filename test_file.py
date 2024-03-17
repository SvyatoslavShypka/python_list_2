import sys

def lines_with_code(lines, code):
    result = []
    for line in lines:
        line = line.rstrip().lstrip('\ufeff')
        data = line.split()
        if len(data) < 8:
            raise RuntimeError("Nieprawidłowe dane")
        indeks = len(data) - 2
        if data[indeks] == code:
            result.append(line)
    return result

if __name__ == '__main__':
    code = sys.stdin.readline().strip()
    if not code.isdigit() or not 100 <= int(code) < 600:
        raise RuntimeError("Kod odpowiedzi HTTP musi być liczbą całkowitą między 100 a 599")

    processed_output = lines_with_code(sys.stdin, code)

    # Łączymy w jeden string
    processed_text = '\n'.join(processed_output)
    # Wyprowadzamy na stdout
    sys.stdout.buffer.write(processed_text.encode())
