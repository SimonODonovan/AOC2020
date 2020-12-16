import copy
import utils

ACC = 'acc'
JMP = 'jmp'
NOP = 'nop'
accumulator = 0
program_counter = 0
instructions_visited = list()
boot_instructions = utils.read_input('8_game_boot_input.txt', str)

def interpret_instruction(instruction):
    command, data = instruction.split(' ')
    return command, int(data)

def execute_instruction(command, data):
    global accumulator
    global program_counter

    if program_counter in instructions_visited:
        return True
    else:
        instructions_visited.append(program_counter)

    if command == ACC:
        accumulator += data
        program_counter += 1
    elif command == JMP:
        program_counter += data
    elif command == NOP:
        program_counter += 1

def attempt_boot(boot_instructions):
    booting = True
    while booting:
        current_instruction = boot_instructions[program_counter]
        command, data = interpret_instruction(current_instruction)
        instruction_collision = execute_instruction(command, data)
        if instruction_collision:
            booting = False

def update_instructions(index, instructions_copy):
    line = instructions_copy[index]
    if 'jmp' in line:
        instructions_copy[index] = 'nop' + line[3:]
    elif 'nop' in line:
        instructions_copy[index] = 'jmp' + line[3:]
    return instructions_copy

# Part 1
attempt_boot(boot_instructions)
print(accumulator)

# Part 2
for index, line in enumerate(boot_instructions):
    accumulator = 0
    program_counter = 0
    instructions_visited = list()

    if NOP in line or JMP in line:
        instructions_copy = copy.deepcopy(boot_instructions)
        updated_instructions = update_instructions(index, instructions_copy)
        try:
            attempt_boot(updated_instructions)
        except IndexError:
            print(accumulator)
