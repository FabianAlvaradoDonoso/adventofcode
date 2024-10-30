from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def area_box(self, large, width, height):
        return 2 * large * width + 2 * width * height + 2 * height * large

    def min_area(self, large, width, height):
        return min([large * width, width * height, height * large])

    def part1(self, data):
        paper = 0
        for box in data:
            large, width, height = box.split("x")
            large, width, height = int(large), int(width), int(height)

            paper += self.area_box(large, width, height)
            paper += self.min_area(large, width, height)

        return paper

    def part2(self, data):
        ribbon = 0
        for box in data:
            large, width, height = box.split("x")
            large, width, height = int(large), int(width), int(height)

            ribbon += large * width * height
            [a, b] = sorted([large, width, height])[:2]
            ribbon += 2 * a + 2 * b

        return ribbon
