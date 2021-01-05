import utils

joltage_input = utils.read_input('10_adapter_array_input.txt', int)
sorted_joltage_input = sorted(joltage_input)

# Part 1
one_step_adapters = 0
three_step_adapters = 1  # include the adapter in the device itself
previous = 0
for idx, adapter_joltage in enumerate(sorted_joltage_input):
    step = adapter_joltage - previous
    previous = adapter_joltage
    if step == 1:
        one_step_adapters += 1
    elif step == 3:
        three_step_adapters += 1
    else:
        raise Exception('Invalid joltage step found at index %s.' % idx)
print(one_step_adapters * three_step_adapters)
