def get_range_set(range_string):
    assignment = range_string.split('-')
    assignment_range = range(int(assignment[0]), int(assignment[1])+1)
    return set(assignment_range)

def read_file(filepath):

    overlap_counter = 0

    with open(filepath) as f:
            for line in f:

                # Split the line into each assignment
                assignment_list = line.strip().split(',')

                # Turn the assignment into a set object
                first_range_set = get_range_set(assignment_list[0])
                second_range_set = get_range_set(assignment_list[1])

                # Check if one of the sets is a subset of the other set
                if first_range_set.issubset(second_range_set) or second_range_set.issubset(first_range_set):
                    print("Subset found")
                    overlap_counter += 1

                print("Current counter status is " + str(overlap_counter))
                    
    return overlap_counter

print(read_file('input.txt'))
