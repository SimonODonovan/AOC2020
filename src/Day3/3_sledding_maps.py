from functools import reduce

##################################################
# AOC 2020 - https://adventofcode.com/2020/day/3 #
##################################################

class SleddingMapDetailer():
    slope1_pos = 0
    slope2_pos = 0
    slope3_pos = 0
    slope4_pos = 0
    slope5_pos = 0
    slope1_trees = 0
    slope2_trees = 0
    slope3_trees = 0
    slope4_trees = 0
    slope5_trees = 0
    map_line_length = 31

    def update_all_slope_positions(self, slope_row):
        self.slope1_pos = self.__update_slope_position(self.slope1_pos, 1)
        self.slope2_pos = self.__update_slope_position(self.slope2_pos, 3)
        self.slope3_pos = self.__update_slope_position(self.slope3_pos, 5)
        self.slope4_pos = self.__update_slope_position(self.slope4_pos, 7)
        if slope_row % 2:
            self.slope5_pos = self.__update_slope_position(self.slope5_pos, 1)

    def __update_slope_position(self, old_pos, leap):
        new_pos = old_pos + leap
        if new_pos >= self.map_line_length:
            new_pos = new_pos - self.map_line_length
        return new_pos

    def update_trees_encountered(self, line, slope_row):
        self.slope1_trees += 1 if line[self.slope1_pos] == '#' else 0
        self.slope2_trees += 1 if line[self.slope2_pos] == '#' else 0
        self.slope3_trees += 1 if line[self.slope3_pos] == '#' else 0
        self.slope4_trees += 1 if line[self.slope4_pos] == '#' else 0
        if not slope_row % 2:
            self.slope5_trees += 1 if line[self.slope5_pos] == '#' else 0

    def calculate_slope_details(self, path):
        slope_row = 0
        with open(path) as input:
            for line in input:
                line = line[:-1]  # remove \n
                self.update_trees_encountered(line, slope_row)
                self.update_all_slope_positions(slope_row)
                slope_row += 1
        slope_trees = [self.slope1_trees, self.slope2_trees, self.slope3_trees,
                       self.slope4_trees, self.slope5_trees]
        return reduce((lambda x, y: x*y), slope_trees)

map_path = '3_sledding_maps.txt'
smd = SleddingMapDetailer()
trees_encountered = smd.calculate_slope_details(map_path)
print(trees_encountered)
