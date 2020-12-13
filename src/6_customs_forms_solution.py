import functools
import utils

def get_group_yes_count_anyone(answer_list_anyone):
    # Add each group members "yes" questions.
    f = lambda x,y: x+y
    answers = functools.reduce(f, answer_list_anyone)
    anyone_unique_answers = set(answers)
    anyone_yes_answer_count = len(anyone_unique_answers)
    return anyone_yes_answer_count

def get_group_yes_count_everyone(answer_list_everyone):
    # Intersection of all group members "yes" questions.
    f = lambda x,y: x.intersection(y)
    answers = functools.reduce(f, [set(x) for x in answer_list_everyone])
    everyone_yes_answer_count = len(answers)
    return everyone_yes_answer_count

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

# Part 1
group_yes_counts = [get_group_yes_count_anyone(group_answers) for group_answers in groups_answers]
print(sum(group_yes_counts))

# Part 2
group_yes_counts = [get_group_yes_count_everyone(group_answers) for group_answers in groups_answers]
print(sum(group_yes_counts))
