from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    @staticmethod
    def is_safe(row):
        inc = [row[i + 1] - row[i] for i in range(len(row) - 1)]
        if set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}:
            return True
        return False

    def part1(self, data):
        reports = [[int(x) for x in d.split(" ")] for d in data]

        safe_count = sum([self.is_safe(row) for row in reports])
        return safe_count

    def part2(self, data):
        reports = [[int(x) for x in d.split(" ")] for d in data]

        safe_count = sum(
            [
                any([self.is_safe(row[:i] + row[i + 1 :]) for i in range(len(row))])  # noqa
                for row in reports
            ]
        )
        return safe_count
