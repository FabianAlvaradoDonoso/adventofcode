from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        lefts = []
        rights = []
        for d in data:
            left, right = d.split("   ")
            lefts.append(int(left))
            rights.append(int(right))

        lefts.sort()
        rights.sort()

        diff = [abs(lefts[i] - rights[i]) for i in range(len(lefts))]

        return sum(diff)

    def part2(self, data):
        lefts = []
        rights = []
        for d in data:
            left, right = d.split("   ")
            lefts.append(int(left))
            rights.append(int(right))

        lefts.sort()
        rights.sort()

        similirity = [lefts[i] * rights.count(lefts[i]) for i in range(len(lefts))]

        return sum(similirity)
