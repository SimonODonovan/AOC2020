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
invalid_number = -1
for idx, current in enumerate(input[25:]):
    is_weak = check_xmas_weakness(current, input[range_min:range_max])
    if is_weak:
        invalid_number = current
        break
    else:
        range_min += 1
        range_max += 1
print(invalid_number)

# Part 2
exploit_range = list()
input.remove(invalid_number)
for idx,val in enumerate(input):
    if exploit_range:
        break
    acc = 0
    for idx2,val2 in enumerate(input[idx:]):
        acc += val2
        if acc == invalid_number:
            range_end = idx+idx2
            exploit_range = input[idx:range_end]
            break
        elif acc > invalid_number:
            break

min = min(exploit_range)
max = max(exploit_range)
exploit = min + max
print(exploit)
