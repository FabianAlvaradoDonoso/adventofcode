from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    @staticmethod
    def solution(data, groups_number):
        data = data[0]
        data_mod = data

        while True:
            group = data_mod[:groups_number]
            sep = list(group)
            sep = list(set(sep))
            if len(sep) == len(group):
                break
            else:
                data_mod = data_mod[1:]

        group = "".join(group)
        index = data.index(group)
        return index + groups_number

    def part1(self, data):
        return self.solution(data, 4)

    def part2(self, data):
        return self.solution(data, 14)
