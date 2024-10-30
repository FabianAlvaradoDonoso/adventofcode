from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    @staticmethod
    def solution(data):
        houses = [(0, 0)]

        for direction in data:
            x, y = houses[-1]

            if direction == "^":
                y += 1
            elif direction == "v":
                y -= 1
            elif direction == ">":
                x += 1
            elif direction == "<":
                x -= 1

            houses.append((x, y))

        return houses

    def part1(self, data):
        data = data[0]
        data = [x for x in data]
        houses = self.solution(data)
        return len(set(houses))

    def part2(self, data):
        data = data[0]
        data = [x for x in data]

        santa = data[::2]
        robo_santa = data[1::2]

        houses_santa = self.solution(santa)
        houses_robo_santa = self.solution(robo_santa)

        houses = houses_santa + houses_robo_santa
        return len(set(houses))
