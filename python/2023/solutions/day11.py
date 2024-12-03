from utils.solution_base import SolutionBase
from itertools import combinations


class Solution(SolutionBase):
    def get_sum_steps(self, data, factor=1):
        universe = [list(line) for line in data]
        empty_rows = [
            index for index, row in enumerate(universe) if "." in row and "#" not in row
        ]
        empty_cols = [
            index
            for index, column in enumerate(zip(*universe))
            if all(cell == "." and "#" not in cell for cell in column)
        ]
        galaxies = [
            (i, j)
            for i, galaxy in enumerate(universe)
            for j, cell in enumerate(galaxy)
            if cell == "#"
        ]
        _sum = 0
        for i in range(len(galaxies) - 1):
            for j in range(i + 1, len(galaxies)):
                y1, x1 = galaxies[i]
                y2, x2 = galaxies[j]

                y1, y2 = sorted([y1, y2])
                x1, x2 = sorted([x1, x2])

                w = x2 - x1
                h = y2 - y1

                cols = sum([1 for c in empty_cols if x1 < c < x2])
                rows = sum([1 for r in empty_rows if y1 < r < y2])
                expansion_factor = (factor - 1) * (cols + rows)

                _sum += w + h + expansion_factor
        return _sum

    def part1(self, data):
        return self.get_sum_steps(data, 2)

    def part2(self, data):
        return self.get_sum_steps(data, 1000000)
