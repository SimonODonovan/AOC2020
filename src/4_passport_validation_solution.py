import re

##################################################
# AOC 2020 - https://adventofcode.com/2020/day/4 #
##################################################

def validate_passport(passport):
    is_valid = False
    validation_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    required_fields_present = all(field in passport for field in validation_fields)
    if required_fields_present:
        is_valid = all(
            [_validate_birth_year(passport),
            _validate_issue_year(passport),
            _validate_expiry_year(passport),
            _validate_height(passport),
            _validate_hair_colour(passport),
            _validate_eye_colour(passport),
            _validate_passport_id(passport)])
    return is_valid

def _validate_birth_year(passport):
    return 1920 <= int(passport['byr']) <= 2002

def _validate_issue_year(passport):
    return 2010 <= int(passport['iyr']) <= 2020

def _validate_expiry_year(passport):
    return 2020 <= int(passport['eyr']) <= 2030

def _validate_height(passport):
    ret = False
    match = re.fullmatch(r'(\d{2,3})(\w{2})', passport['hgt'])
    if match:
        height = int(match.groups()[0])
        unit = match.groups()[1]
        if unit == 'cm':
            ret = (150 <= height <= 193)
        if unit == 'in':
            ret = (59 <= height <= 76)
    return ret

def _validate_hair_colour(passport):
    return re.fullmatch('#[0-9a-f]{6}', passport['hcl'])

def _validate_eye_colour(passport):
    valid_eye_colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return passport['ecl'] in valid_eye_colours

def _validate_passport_id(passport):
    return re.fullmatch(r'^[0-9]{9}$', passport['pid'])

valid_passport_count = 0
passport_input = '4_passport_validation_input.txt'
with open(passport_input) as passport_input:
    current_passport = dict()
    for line in passport_input:
        if line == '\n':
            is_valid = validate_passport(current_passport)
            valid_passport_count +=1 if is_valid else 0
            current_passport = dict() # reset on empty line
        else:
            line_kv_pairs = dict(kv.split(':') for kv in line.split()) # split on whitespace, then key:val
            current_passport = current_passport | line_kv_pairs # combine dictionaries
print(valid_passport_count)
