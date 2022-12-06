def replace_characters_in_stack(stacks_list):
    # Provide a list of characters we want to remove from each entry in the list
    character_list = [' ', '[', ']']
    
    # Loop through all characters to remove from each row of the the stack
    for character in character_list:
        stacks_list = [stack.replace(character, '') for stack in stacks_list]
    
    return stacks_list

def follow_instruction(stacks, instruction):
    instruction_list = instruction.strip().split()
    # Number of crates to move is in position 1
    # Origin stack column is in position 3
    # Destination stack column is in position 5

    # Number of crates to move will dictate the size of our loop
    crates = 0
    max_crates = int(instruction_list[1])
    # Make an extra list to keep the crates in order
    crane_crates = []

    # Loop through the column and remove the crates one at a time to maintain order
    while crates < max_crates:
        crate_to_move = stacks[int(instruction_list[3])-1].pop(0)
        crane_crates.append(crate_to_move)
        crates += 1

    # Loop backwards through the iterator, inserting the crates one at a time to maintain order
    while crates >= 1:
        stacks[int(instruction_list[5])-1].insert(0, crane_crates[crates-1])
        crates -= 1

    return stacks


with open('input.txt') as file:

    stacks, instructions = file.read().split('\n\n')
    stacks, instructions = stacks.split('\n'), instructions.split('\n')

    stacks = [stack.replace('    ', '!') for stack in stacks]
    stacks = replace_characters_in_stack(stacks)

    #Remove last entry which is the labels for the columns and empty space for instructions 
    stacks = stacks[:-1]
    instructions = instructions[:-1]

    stack_columns = [[], [], [], [], [], [], [], [], []]

    # Loop through each row and turn them into lists of vertical columns 1-9
    for i in range(0, len(stacks[4]), 1):
        for j in range (0, len(stacks), 1):
            #We filter out the 'blank' crates at this point
            if stacks[j][i] != '!':
                stack_columns[i].append(stacks[j][i])

    for instruction in instructions:
        stack_columns = follow_instruction(stack_columns, instruction)

    answer = ''
    # Print top crate in each column for the solution
    for column in stack_columns:
        answer += column[0]
    print(answer)




