import sys
import fileinput


def process_all_lines(lines):
    # Zwracamy wszystkie linie bez zmian
    return lines

# if __name__ == '__main__':
processed_output = []
for fileinput_line in fileinput.input():
    fileinput_line = fileinput_line.rstrip().lstrip('\ufeff')
    if 'Exit' == fileinput_line.rstrip():
        break
    processed_output.append(process_all_lines(fileinput_line))
# Złączamy w jeden String
processed_text = '\n'.join(processed_output)
# Wyprowadzamy na stdout
sys.stdout.buffer.write(processed_text.encode())
