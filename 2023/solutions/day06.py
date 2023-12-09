from utils.solution_base import SolutionBase
import re


class Solution(SolutionBase):
    def part1(self, data):
        times = [int(time.strip()) for time in data[0].split(" ") if time.isdigit()]
        distances = [
            int(distance.strip())
            for distance in data[1].split(" ")
            if distance.isdigit()
        ]

        multiplier = 1
        for index, time in enumerate(times):
            distance = distances[index]

            ways_to_win = 0
            for x in range(0, time):
                if x * (time - x) > distance:
                    ways_to_win += 1

            multiplier *= ways_to_win

        return multiplier

    def part2(self, data):
        times = [int("".join(re.findall(r"\d", data[0])))]
        distances = [int("".join(re.findall(r"\d", data[1])))]

        multiplier = 1
        for index, time in enumerate(times):
            distance = distances[index]

            ways_to_win = 0
            for x in range(0, time):
                if x * (time - x) > distance:
                    ways_to_win += 1

            multiplier *= ways_to_win

        return multiplier
