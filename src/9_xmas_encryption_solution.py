import utils

input = utils.read_input('9_xmas_encryption_input.txt', int)

range_min = 0
range_max = 25
step = 0

def check_xmas_weakness(current, preamble):
    search_set = set(preamble)
    for num in preamble:
        match_found = current - num in search_set
        if match_found:
            return False
    return True

# Part 1
for idx, current in enumerate(input[25:]):
    is_weak = check_xmas_weakness(current, input[range_min:range_max])
    if is_weak:
        print(current)
        break
    else:
        range_min += 1
        range_max += 1

# Part 2