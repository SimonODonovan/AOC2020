import re
import utils

##################################################
# AOC 2020 - https://adventofcode.com/2020/day/2 #
##################################################

def get_password_policy(line):
    validation_numbers = re.findall('[0-9]+', line)
    validation_letter = re.search(r"\s(\w)\W\s", line).group(1)
    primary = int(validation_numbers[0])
    secondary = int(validation_numbers[1])
    return (primary, secondary, validation_letter)

def get_password(line):
    return line.split(' ')[2]

def is_valid_password_old(password_policy, password):
    _min, _max, letter = password_policy
    valid_letters_count = len(re.findall(letter, password))
    return (_min <= valid_letters_count) and  (_max >= valid_letters_count)

input_list = utils.read_input('2_password_validation_input.txt', str)
valid_password_count_old = 0
for password_details in input_list:
    password_policy = get_password_policy(password_details)
    password = get_password(password_details)
    is_valid = is_valid_password_old(password_policy, password)
    if is_valid:
        valid_password_count_old += 1
print(valid_password_count_old)

def is_valid_password_toboggan(password_policy, password):
    ret = False
    primary, secondary, validation_letter = password_policy
    _sum = primary + secondary
    _max = primary if primary > secondary else secondary
    _min = _sum - _max
    pass_len = len(password)
    if pass_len >= _max:
        split_pass = re.split('', password)
        primary_pass_char = split_pass[primary]
        secondary_pass_char = split_pass[secondary]
        valid_primary = validation_letter == primary_pass_char
        valid_secondary = validation_letter == secondary_pass_char
        valid_duplicate = valid_primary != valid_secondary
        ret = valid_duplicate and (valid_primary or valid_secondary)
    return ret

input_list = utils.read_input('2_password_validation_input.txt', str)
valid_password_count_toboggan = 0
for password_details in input_list:
    password_policy = get_password_policy(password_details)
    password = get_password(password_details)
    is_valid = is_valid_password_toboggan(password_policy, password)
    if is_valid:
        valid_password_count_toboggan += 1
print(valid_password_count_toboggan)
