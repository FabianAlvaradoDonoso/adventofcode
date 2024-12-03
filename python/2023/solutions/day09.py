from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        suma_historia = 0

        for index, historia in enumerate(data):
            valores = [int(v) for v in historia.split(" ")]
            diff = [valores]

            while not all(valor == 0 for valor in diff[-1]):
                new_diff = []
                for i in range(len(diff[-1]) - 1):
                    new_diff.append(int(diff[-1][i + 1]) - int(diff[-1][i]))
                diff.append(new_diff)

            diff = diff[::-1]

            anterior = 0
            suma = 0
            for i in range(len(diff)):
                ultimo = diff[i][-1] + anterior
                diff[i].append(ultimo)
                anterior = diff[i][-1]

                if i == len(diff) - 1:
                    suma_historia += ultimo

        return suma_historia

    def part2(self, data):
        suma_historia = 0
        for index, historia in enumerate(data):
            valores = [int(v) for v in historia.split(" ")]
            diff = [valores[::-1]]

            while not all(valor == 0 for valor in diff[-1]):
                new_diff = []
                for i in range(len(diff[-1]) - 1):
                    new_diff.append(int(diff[-1][i]) - int(diff[-1][i + 1]))
                diff.append(new_diff)

            # reverse diff list
            diff = diff[::-1]

            anterior = 0
            suma = 0
            for i in range(len(diff)):
                ultimo = diff[i][-1] - anterior
                diff[i].append(ultimo)
                anterior = diff[i][-1]

                if i == len(diff) - 1:
                    suma_historia += anterior

        return suma_historia
