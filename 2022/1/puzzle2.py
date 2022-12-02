def read_file(filepath):
    currentCals = 0
    caloriesList = []

    with open(filepath) as f:
        for line in f:
            if line != '\n':
                currentCals += int(line)
            else:
                caloriesList.append(currentCals)
                currentCals = 0

    caloriesList.sort(reverse=True)
    return caloriesList[0]+caloriesList[1]+caloriesList[2]

print(read_file('input1.txt'))