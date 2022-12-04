def build_priorities_dict(item_list):
    priority_dictionary = {}

    # Loop through once to assign the priorities to the lower case item types
    for i in range(1, 27, 1):
        priority_dictionary[item_list[i-1]] = i

    # Loop through a second time to assign the priorities for the upper case item types
    for i in range(1, 27, 1):
        priority_dictionary[item_list[i-1].upper()] = i+26

    return priority_dictionary

def read_file(filepath, priority_dictionary):

    priority_sum = 0
    common_item = ''
    rucksack_list = []

    with open(filepath) as f:

            counter = 0
            for line in f:
                rucksack_list.append(line.strip())
                # Get the length of the line and divide it into its two equal sized compartments

                # After we have a set of 3 lines in the list, start comparing them
                if counter == 2:

                    first_set = {1}
                    second_set = {2}
                    third_set = {3} 

                    for item in rucksack_list[0]:
                        first_set.add(item)
                    
                    for item in rucksack_list[1]:
                        second_set.add(item)

                    for item in rucksack_list[2]:
                        third_set.add(item)

                    # Get intersections of first and second lines, then second and third lines, then take
                    # the intersection of those intersections
                    first_intersection = first_set.intersection(second_set)
                    second_intersection = second_set.intersection(third_set)
                    final_intersection = first_intersection.intersection(second_intersection)

                    common_item = "".join(final_intersection)
                    priority_sum += priority_dictionary[common_item]

                    # Clean up the list and counter for the next iteration
                    rucksack_list.clear()
                    counter = 0
                else:
                    # If we aren't at a complete set of three lines, increment the counter and go to the next line
                    counter += 1
    return priority_sum

item_types = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

priorities_dict = build_priorities_dict(item_types)

total_priority = read_file('input.txt', priorities_dict)
print(total_priority)
