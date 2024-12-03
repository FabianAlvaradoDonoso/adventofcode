from utils.solution_base import SolutionBase
import re


class Solution(SolutionBase):
    @staticmethod
    def get_draw(data):
        stack = []
        for line in data:
            if "1" in line:
                break

            line = line.replace(" ", "*")
            line = line.replace("****", "*[0]")

            for index, char in enumerate(line):
                if index == 0 and char == "*":
                    line = "[0]*" + line[4:]

            if line != "":
                stack.append(line)
        return stack

    @staticmethod
    def clear_draw(draw):
        new_stack = []
        for stack in draw:
            stack = stack.split("*")
            stack = [i.replace("[", "").replace("]", "") for i in stack if i != ""]
            new_stack.append(stack)
        return new_stack

    @staticmethod
    def get_instructions(data):
        instructions = [d for d in data if "move" in d]
        instructions = [re.findall(r"\d+", i) for i in instructions]
        instructions = [list(map(int, i)) for i in instructions]

        return instructions

    @staticmethod
    def get_solution(data, order):
        draw = Solution.get_draw(data)
        draw = Solution.clear_draw(draw)
        draw = list(map(list, zip(*draw)))
        instructions = Solution.get_instructions(data)

        new_draw = []
        for d in draw:
            new = []
            for i in d:
                if i != "0":
                    new.append(i)
            new_draw.append(new)

        draw = new_draw

        for i in instructions:
            [quantity_, from_, to_] = i
            move = draw[from_ - 1][:quantity_]
            if order:
                move = move[::-1]
            draw[from_ - 1] = draw[from_ - 1][quantity_:]
            draw[to_ - 1] = move + draw[to_ - 1]

        first = ""
        for d in draw:
            first += d[0]

        return first

    def part1(self, data):
        return Solution.get_solution(data, True)

    def part2(self, data):
        return Solution.get_solution(data, False)
