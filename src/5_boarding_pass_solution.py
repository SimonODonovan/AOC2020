from math import ceil
import utils

def get_seating(seating_guide, last_pos):
    ret = -1
    lower = 0
    upper = last_pos
    for direction in seating_guide:
        mid = ceil((lower + upper) / 2)
        if direction == 'F' or direction == 'L': # take lower
            upper = mid-1
            ret = upper
        elif direction == 'B' or direction == 'R': # take upper
            lower = mid
            ret = lower
    return ret

def generate_seat_id(row, col):
    seat_id = (row * 8) + col
    return seat_id

seating_instructions_list = utils.read_input('5_boarding_pass_input.txt', str)
max_seat_id = -1
for seating_instruction in seating_instructions_list:
    row = get_seating(seating_instruction[0:-3], 127)
    col = get_seating(seating_instruction[-3:], 7)
    seat_id = generate_seat_id(row, col)
    if seat_id > max_seat_id:
        max_seat_id = seat_id
print(max_seat_id)