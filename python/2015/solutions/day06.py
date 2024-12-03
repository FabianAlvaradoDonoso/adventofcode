from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        grid = [[0 for _ in range(1000)] for _ in range(1000)]
        for line in data:
            type = len(line.split(" "))
            if type == 4:  # noqa: PLR2004
                action, start, _, end = line.split(" ")
            else:
                _, action, start, _, end = line.split(" ")

            start = list(map(int, start.split(",")))
            end = list(map(int, end.split(",")))

            if action == "on":
                for i in range(start[0], end[0] + 1):
                    for j in range(start[1], end[1] + 1):
                        grid[i][j] = 1

            elif action == "off":
                for i in range(start[0], end[0] + 1):
                    for j in range(start[1], end[1] + 1):
                        grid[i][j] = 0

            elif action == "toggle":
                for i in range(start[0], end[0] + 1):
                    for j in range(start[1], end[1] + 1):
                        grid[i][j] = 1 - grid[i][j]

        return sum([sum(row) for row in grid])

    def part2(self, data):
        grid = [[0 for _ in range(1000)] for _ in range(1000)]
        for line in data:
            type = len(line.split(" "))
            if type == 4:  # noqa: PLR2004
                action, start, _, end = line.split(" ")
            else:
                _, action, start, _, end = line.split(" ")

            start = list(map(int, start.split(",")))
            end = list(map(int, end.split(",")))

            if action == "on":
                for i in range(start[0], end[0] + 1):
                    for j in range(start[1], end[1] + 1):
                        grid[i][j] = grid[i][j] + 1

            elif action == "off":
                for i in range(start[0], end[0] + 1):
                    for j in range(start[1], end[1] + 1):
                        if grid[i][j] > 0:
                            grid[i][j] = grid[i][j] - 1

            elif action == "toggle":
                for i in range(start[0], end[0] + 1):
                    for j in range(start[1], end[1] + 1):
                        grid[i][j] = grid[i][j] + 2

        return sum([sum(row) for row in grid])
