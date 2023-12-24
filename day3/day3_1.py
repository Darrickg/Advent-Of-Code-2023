# edge case 1: first line only needs to read first and second line

# logic:
# get all numbers and starting index in a line
# check the index range +-1 for any symbols

# edge case 2: last line only needs to read last and previous line

import re

file = 'day3.txt'
read_file = open(file, 'r')

test_string = "467..114..##"

def get_numbers_index_length(line):
    numbers_info = {}

    numbers_and_symbols = re.finditer(r'[0-9*%#]+', line)

    for match in numbers_and_symbols:
        number = match.group()
        length = len(number)
        start_index = match.start()
        numbers_info[number] = {'length': length, 'start_index': start_index}

    return numbers_info



print(get_numbers_index_length(test_string))