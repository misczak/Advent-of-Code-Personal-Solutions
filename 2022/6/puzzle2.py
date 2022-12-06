def move_list(list, new_element):
    # When we need to add a new value, remove the first element and add the new element to the end of the list
    list.pop(0)
    list.append(new_element)
    return list

def check_duplicates(list):
    # Turn list into a set which removes duplicates, and see if it is the same size as the original list
    return len(list) != len(set(list))

counter = 0
datastream = []
duplicates_exist = True

with open('input.txt') as f:
    while duplicates_exist:
        counter += 1
        # Read one character at a time
        char = f.read(1)

        if not char:
            print('Reached end of file')
            break

        # Boostrap the list with the first fourteen values
        if counter <= 14:
            datastream.append(char)
        else:
            # After the first fourteen values, start checking for duplicates and moving the list accordingly
            datastream = move_list(datastream, char)
            duplicates_exist = check_duplicates(datastream)
            # else:
            #     print('Start of Packet found at position ' + str(counter))
            #     break
        
print('Start of packet is found at ' + str(counter))