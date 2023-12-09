from utils.solution_base import SolutionBase
import re


class Solution(SolutionBase):
    @staticmethod
    def get_number_games(line):
        game = re.findall(r"\d", line)
        return int("".join(game))

    @staticmethod
    def split_string_strip(string, separator):
        return [s.strip() for s in string.split(separator)]

    @staticmethod
    def power_set(bag):
        power_set = 1
        for key in bag:
            power_set *= bag[key]  # + 1
        return power_set

    def part1(self, data):
        bag = {
            "red": 12,
            "green": 13,
            "blue": 14,
        }

        sum_id_games = 0
        for line in data:
            flag = True
            [game, set_cubes] = line.split(":")

            game = Solution.get_number_games(game)

            for set in Solution.split_string_strip(set_cubes, ";"):
                for cube in Solution.split_string_strip(set, ","):
                    [count, color] = Solution.split_string_strip(cube, " ")
                    flag = flag and bag[color] >= int(count)

            sum_id_games += game if flag else 0

        return sum_id_games

    def part2(self, data):
        sum = 0
        for line in data:
            bag = {
                "red": 0,
                "green": 0,
                "blue": 0,
            }
            flag = True
            [game, set_cubes] = line.split(":")

            game = Solution.get_number_games(game)

            for set in Solution.split_string_strip(set_cubes, ";"):
                for cube in Solution.split_string_strip(set, ","):
                    [count, color] = Solution.split_string_strip(cube, " ")
                    bag[color] = int(count) if int(count) > bag[color] else bag[color]

            sum += Solution.power_set(bag) if flag else 0
