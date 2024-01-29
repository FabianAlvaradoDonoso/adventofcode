from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        sumas = [sum([int(x) for x in elf.split("\n")]) for elf in elves]
        return max(sumas)

    def part2(self, data):
        sumas = [sum([int(x) for x in elf.split("\n")]) for elf in elves]
        sumas.sort(reverse=True)
        return sum(sumas[:3])
