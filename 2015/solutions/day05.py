from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        count = 0
        min_vowels = 3
        for d in data:
            vowels = 0
            double = False
            bad = False
            for i in range(len(d)):
                if d[i] in "aeiou":
                    vowels += 1
                if i > 0 and d[i] == d[i - 1]:
                    double = True
                if i > 0 and d[i - 1 : i + 1] in ["ab", "cd", "pq", "xy"]:  # noqa
                    bad = True
            if vowels >= min_vowels and double and not bad:
                count += 1
        return count

    def part2(self, data):
        count = 0
        for d in data:
            pair = False
            repeat = False

            for i in range(len(d) - 1):
                if d.count(d[i] + d[i + 1]) > 1:
                    pair = True
                    break

            for i in range(len(d) - 2):
                if d[i] == d[i + 2]:
                    repeat = True
                    break

            if pair and repeat:
                count += 1

        return count
