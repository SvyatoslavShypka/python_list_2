import re

code_200 = 0
code_302 = 0
code_404 = 0
counter = 0

# file_name = input("Podaj nazwę pliku:")
# word = input("Podaj numer kodu:")
file_name = "NASA"
word = "200"
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\" ".format(word),line):
             code_1 = 0
             code_1 = code_1 + 1
             print(code_1)
             return True
   return False

# if find_string(file_name, word):
#     print("found")
#     for line in open(file_name):
#         code_200 = code_200 + 1
# else:
#     print("Code wasn't found")
# print(code_200)

# if re.search(r"\" 200"gm.format(word),line):
