def read_input(path, type):
    lines = list()
    with open(path) as input:
        for line in input:
            lines.append(type(line.rstrip('\n')))
    return lines
