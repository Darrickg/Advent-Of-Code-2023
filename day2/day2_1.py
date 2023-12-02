file = 'day2.txt'
read_file = open(file, 'r')

total = 0

for line in read_file:
    colour_max = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    line = line.rstrip("\n")

    game = line.split(": ")
    rounds = game[1].split("; ")

    game_num = game[0].split(" ")
    
    for round in rounds:
        colours = round.split(", ")

        for colour in colours:
            number = colour.split(" ")
            
            if number[1] == "red":

                if colour_max["red"] < int(number[0]):
                    colour_max["red"] = int(number[0])

            if number[1] == "blue":

                if colour_max["blue"] < int(number[0]):
                    colour_max["blue"] = int(number[0])

            if number[1] == "green":

                if colour_max["green"] < int(number[0]):
                    colour_max["green"] = int(number[0])

    if (colour_max["red"] <=  12) and (colour_max["blue"] <= 14) and (colour_max["green"] <= 13):
        total += int(game_num[1])


print(total)