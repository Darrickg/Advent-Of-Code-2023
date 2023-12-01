with open("day1.txt") as file:
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    part1 = 0
    part2 = 0

    for row in file:
        numbers1 = []
        numbers2 = []
        i = 0

        while i < len(row):

            if row[i].isdigit():
                numbers1.append(row[i])
                numbers2.append(row[i])

            for word in words:
                if i < len(row) - len(word) and row[i:i + len(word)] == word:
                    numbers2.append(words.index(word) + 1)

            i += 1

        part1 += int(f"{numbers1[0]}{numbers1[-1]}")
        part2 += int(f"{numbers2[0]}{numbers2[-1]}")
        
    print(part1)
    print(part2)