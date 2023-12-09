from utils.solution_base import SolutionBase
import re


class Solution(SolutionBase):
    @staticmethod
    def transform(text, part):
        word_number = {
            "one": "on1ne",
            "two": "tw2wo",
            "three": "thr3ree",
            "four": "fou4our",
            "five": "fiv5ive",
            "six": "si6ix",
            "seven": "sev7ven",
            "eight": "eig8ght",
            "nine": "nin9ine",
        }
        if part == 2:
            for word, number in word_number.items():
                text = text.replace(word, number)
        numbers = re.findall(r"\d+", text)
        return int(numbers[0][0] + numbers[-1][-1])

    def part1(self, data):
        return sum([Solution.transform(text, part=1) for text in data])

    def part2(self, data):
        return sum([Solution.transform(text, part=2) for text in data])
