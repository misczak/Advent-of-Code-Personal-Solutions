def read_file(filepath):
    currentCals = 0
    topCals = 0

    with open(filepath) as f:
        for line in f:
            if line != '\n':
                currentCals += int(line)
            else:
                if currentCals > topCals:
                    topCals = currentCals
                currentCals = 0
    return topCals

print(read_file('input1.txt'))