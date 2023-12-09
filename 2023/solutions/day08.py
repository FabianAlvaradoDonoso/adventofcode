from utils.solution_base import SolutionBase
import math


class Solution(SolutionBase):
    @staticmethod
    def convert_data(data):
        result_dict = {}
        for line in data:
            parts = line.split(" = ")
            key = parts[0]
            values_str = parts[1].strip("()")
            values_list = [v.strip() for v in values_str.split(",")]
            result_dict[key] = values_list
        return result_dict

    def part1(self, data):
        secuencia = data[0]
        nodos = data[2:]

        nodos = Solution.convert_data(nodos)

        primero = "AAA"
        ultimo = "ZZZ"

        step = 0
        contador = 0
        while step < len(secuencia):
            contador += 1
            left, right = nodos[primero]

            if secuencia[step] == "R":
                primero = right
            else:
                primero = left

            if primero == ultimo:
                break

            step += 1
            if step == len(secuencia):
                step = 0

        return contador

    def part2(self, data):
        secuencia = data[0]
        nodos = data[2:]

        inst = list(secuencia)
        _map = {}
        for line in nodos:
            node, nexts = line.split(" = ")
            _map[node] = {k: v for k, v in zip(["L", "R"], nexts[1:-1].split(", "))}

        curr = [node for node in _map.keys() if node.endswith("A")]
        inst_idx = 0
        steps = 0

        least_steps = [0] * len(curr)

        while 0 in least_steps:
            for i, node in enumerate(curr):
                if node.endswith("Z") and least_steps[i] == 0:
                    least_steps[i] = steps

            curr = [_map[node][inst[inst_idx]] for node in curr]
            inst_idx = (inst_idx + 1) % len(inst)
            steps += 1

        return math.lcm(*least_steps)
