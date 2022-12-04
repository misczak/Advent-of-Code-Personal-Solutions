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

    with open(filepath) as f:
            for line in f:

                # Get the length of the line and divide it into its two equal sized compartments
                line_length = len(line.strip())
                compartment_size = int(line_length / 2)
                first_compartment = line[0:compartment_size]
                second_compartment = line[compartment_size:-1]
                
                # Set up two sets and then fill them with unique items from each compartment
                first_set = {1}
                second_set = {2}
                for i in first_compartment:
                    first_set.add(i)
                
                for i in second_compartment:
                    second_set.add(i)

                # Turn the set intersection result into a string
                common_item = "".join(first_set.intersection(second_set))

                # Add the priority of the common item to the running total 
                priority_sum += priority_dictionary[common_item]

    return priority_sum

item_types = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

priorities_dict = build_priorities_dict(item_types)

total_priority = read_file('input.txt', priorities_dict)
print(total_priority)
