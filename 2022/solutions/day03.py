from utils.solution_base import SolutionBase

UPPERCASE_DELTA = 38
LOWERCASE_DELTA = 96


class Solution(SolutionBase):
    def part1(self, data):
        sum = 0
        for line in data:
            length = len(line)
            first_part = line[: length // 2]
            second_part = line[length // 2 :]

            first_part = list(set(first_part))
            second_part = list(set(second_part))

            chars = []
            for char in first_part:
                if char in second_part:
                    chars.append(char)

            for char in chars:
                if char.isupper():
                    sum += ord(char) - UPPERCASE_DELTA
                else:
                    sum += ord(char) - LOWERCASE_DELTA

        return sum

    def part2(self, data):
        sum = 0

        size_group = 3
        for i in range(0, len(data), size_group):
            group = []
            for group_index in range(size_group):
                line = data[i + group_index]
                line = list(set(line))
                group.append(line)

            chars = []
            for group_index in range(size_group):
                for char in group[group_index]:
                    char_in_all = True
                    for group_index2 in range(size_group):
                        if group_index != group_index2:
                            if char not in group[group_index2]:
                                char_in_all = False
                                break
                    if char_in_all:
                        chars.append(char)

            chars = list(set(chars))

            for char in chars:
                if char.isupper():
                    sum += ord(char) - UPPERCASE_DELTA
                else:
                    sum += ord(char) - LOWERCASE_DELTA

        return sum
