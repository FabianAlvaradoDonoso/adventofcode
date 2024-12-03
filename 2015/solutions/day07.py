from utils.solution_base import SolutionBase

CIRCUIT = {}
EVALUATED = {}


class Solution(SolutionBase):
    @staticmethod
    def parse_input(data):
        for line in data:
            ops, wire = line.split(" -> ")
            CIRCUIT[wire] = ops.split(" ")

    def evaluate(self, wire: str) -> int:
        try:
            return int(wire)
        except ValueError:
            pass

        result = 0
        if wire not in EVALUATED:
            ops = CIRCUIT[wire]

            # single value
            if len(ops) == 1:
                result = self.evaluate(ops[0])
            else:
                op = ops[-2]
                if op == "AND":
                    result = self.evaluate(ops[0]) & self.evaluate(ops[2])
                if op == "OR":
                    result = self.evaluate(ops[0]) | self.evaluate(ops[2])
                if op == "NOT":
                    result = ~self.evaluate(ops[1]) & 0xFFFF
                if op == "RSHIFT":
                    result = self.evaluate(ops[0]) >> self.evaluate(ops[2])
                if op == "LSHIFT":
                    result = self.evaluate(ops[0]) << self.evaluate(ops[2])
            EVALUATED[wire] = result
        return EVALUATED[wire]

    def part1(self, data):
        self.parse_input(data)
        return self.evaluate("a")

    def part2(self, data):
        self.part1(data)
        a = EVALUATED["a"]
        EVALUATED.clear()
        EVALUATED["b"] = a
        return self.evaluate("a")
