from utils.solution_base import SolutionBase
from itertools import count
import hashlib


class Solution(SolutionBase):
    @staticmethod
    def solution(data, start):
        data = data[0]
        for number in count(1):
            key = data + str(number)
            result = hashlib.md5(key.encode())
            if result.hexdigest().startswith(start):
                break
        return number

    def part1(self, data):
        return self.solution(data, "00000")

    def part2(self, data):
        return self.solution(data, "000000")
