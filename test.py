import re

numbers_and_symbols = re.findall(r'[0-9*%#]+', input_string)

print(numbers_and_symbols)
