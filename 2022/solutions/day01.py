from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        elves = []
        sum = 0
        for i in data:
            if i != "":
                sum += int(i)
            else:
                elves.append(sum)
                sum = 0
        elves.append(sum)
        return max(elves)

    def part2(self, data):
        elves = []
        sum = 0
        for i in data:
            if i != "":
                sum += int(i)
            else:
                elves.append(sum)
                sum = 0
        elves.append(sum)
        elves.sort(reverse=True)
        sum = 0
        for i in range(3):
            sum += elves[i]
        return sum
