from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    @staticmethod
    def solution(data, part):
        current_floor = 0
        data = data[0]
        for index, floor in enumerate(data):
            current_floor += 1 if floor == "(" else -1

            if part == 2 and current_floor == -1:  # noqa: PLR2004
                return index + 1

        return current_floor

    def part1(self, data):
        return self.solution(data, 1)

    def part2(self, data):
        return self.solution(data, 2)
