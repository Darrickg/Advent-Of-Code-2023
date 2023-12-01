file = 'day1.txt'
read_file = open(file, 'r')

total = 0

for line in read_file:

    result_string = ''

    for letter in line:

        if letter.isnumeric():
            result_string += letter
            break

    for i in range(len(line)-1, -1, -1):

        if line[i].isnumeric():
            result_string += line[i]
            break

    print(result_string)
    total += int(result_string)

print(total)