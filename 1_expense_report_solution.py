import utils

##################################################
# AOC 2020 - https://adventofcode.com/2020/day/1 #
##################################################

def uniqify(input_list):
    return set(input_list)

def find_entries(input_set):
    for item in input_set:
        remainder = 2020 - item
        if remainder in input_set:
            return item, remainder

input_list = utils.read_input('1_expense_report_input.txt', int)
input_set = uniqify(input_list)
addend1, addend2 = find_entries(input_list)
solution = addend1 * addend2
print(addend1)
print(addend2)
print(solution)
