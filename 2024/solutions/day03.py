from utils.solution_base import SolutionBase
import re


class Solution(SolutionBase):
    def part1(self, data):
        data = "".join(data)

        sum = 0
        matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", data)

        for match in matches:
            numbers = re.findall(r"\d{1,3}", match)
            result = int(numbers[0]) * int(numbers[1])
            sum += result
        return sum

    def part2(self, data):
        data = "".join(data)

        matches = re.finditer(r"don't\(\)|do\(\)|mul\(\d{1,3},\d{1,3}\)", data)
        sum = 0
        active = True
        result = []

        for match in matches:
            if match.group() == "don't()":
                active = False
            elif match.group() == "do()":
                active = True
            elif active and match.group():
                result.append(match.group())

        for match in result:
            numbers = re.findall(r"\d{1,3}", match)
            result = int(numbers[0]) * int(numbers[1])
            sum += result

        return sum
