from collections import defaultdict
import functools
import re
import utils

def create_bag_mapping(bag_details):
    child_parent_bag_mapping = defaultdict(list)  # part 1
    parent_child_bag_mapping = defaultdict(list)  # part 2
    top_level_pattern = r'^(\w+\s\w+) bags'
    sub_level_pattern = r'(\d+) (\w+\s\w+) bag[s]*'
    for bag_detail in bag_details:
        top_level_details, sub_level_details = bag_detail.split('contain')
        top_level_bag = re.match(top_level_pattern, top_level_details).groups()[0]
        for sub_level_detail in sub_level_details.split(','):
            matcher = re.match(sub_level_pattern, sub_level_detail.strip())
            if matcher:
                sub_level_bag_count = matcher.groups()[0]
                sub_level_bag_name = matcher.groups()[1]
                child_parent_bag_mapping[sub_level_bag_name].append(top_level_bag)
                parent_child_bag_mapping[top_level_bag].append((sub_level_bag_name, sub_level_bag_count))
    return child_parent_bag_mapping, parent_child_bag_mapping

def find_bag_parents(bag_names, bag_mapping):
    if not bag_names:
        return []
    else:
        parent_list = list()
        for bag_name in bag_names:
            bag_parents = bag_mapping[bag_name]
            parent_list = parent_list + bag_parents
        return parent_list + find_bag_parents(parent_list, bag_mapping)

def find_bag_children_count(bag_name, bag_mapping):
    count = 0
    for bag_details in bag_mapping.get(bag_name, []):
        count += int(bag_details[1]) + (int(bag_details[1])) * find_bag_children_count(bag_details[0], bag_mapping)
    return count

initial_bag_name = 'shiny gold'
bag_details_input = utils.read_input('7_luggage_processing_input.txt', str)
child_parent_bag_mapping, parent_child_bag_mapping = create_bag_mapping(bag_details_input)

# Part 1
parents = set(find_bag_parents([initial_bag_name], child_parent_bag_mapping))
print(len(parents))

# Part 2
child_count = find_bag_children_count(initial_bag_name, parent_child_bag_mapping)
print(child_count)
