def overlap(first_range, second_range):
    range1 = first_range.split('-')
    range2 = second_range.split('-')
    return int(range1[1]) >= int(range2[0]) and int(range2[1]) >= int(range1[0])

def read_file(filepath):

    overlap_counter = 0

    with open(filepath) as f:
            for line in f:

                # Split the line into each assignment
                assignment_list = line.strip().split(',')

                # Check if the ranges have any overlap 
                if overlap(assignment_list[0], assignment_list[1]):
                    overlap_counter += 1
                
                print("Current counter status is " + str(overlap_counter))     
    return overlap_counter

print(read_file('input.txt'))
