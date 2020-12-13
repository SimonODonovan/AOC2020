import functools
import utils

def get_group_yes_count_anyone(answer_list):
    f = lambda x,y: x+y
    answers = functools.reduce(f, answer_list)
    unique_answers = set(answers)
    group_yes_answer_count = len(unique_answers)
    return group_yes_answer_count

def get_group_yes_count_everyone(answer_list):
    f = lambda x,y: x+y
    answers = functools.reduce(f, answer_list)
    unique_answers = set(answers)
    group_yes_answer_count = len(unique_answers)
    return group_yes_answer_count

def get_answer_groups(answer_input):
    groups_list = list()
    current_group = list()
    for line in answer_input:
        if line == '':
            groups_list.append(current_group)
            current_group = list()
        else:
            current_group.append(line)
    return groups_list

flight_answers = utils.read_input('6_customs_forms_input.txt', str)
groups_answers = get_answer_groups(flight_answers)
group_yes_counts = [get_group_yes_count_anyone(group_answers) for group_answers in groups_answers]
print(sum(group_yes_counts))