from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        sum = 0
        for elves in data:
            [elv1, elv2] = elves.split(",")

            [min1, max1] = [int(x) for x in elv1.split("-")]
            [min2, max2] = [int(x) for x in elv2.split("-")]

            if min1 <= min2 and max1 >= max2 or min2 <= min1 and max2 >= max1:
                sum += 1
        return sum

    def part2(self, data):
        sum = 0
        for elves in data:
            [elv1, elv2] = elves.split(",")

            [min1, max1] = [int(x) for x in elv1.split("-")]
            [min2, max2] = [int(x) for x in elv2.split("-")]

            if min1 <= max2 and max1 >= min2:
                sum += 1
        return sum
