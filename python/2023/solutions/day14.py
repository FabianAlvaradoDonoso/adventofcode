from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        data = [list(line) for line in data]

        for i in range(len(data)):
            for j in range(len(data[i])):
                if i == 0:
                    continue

                if data[i][j] == "O":
                    for k in range(i - 1, -1, -1):
                        if k == 0 and data[k][j] == ".":
                            data[k][j] = "O"
                            data[i][j] = "."
                            break
                        if data[k][j] == "O" or data[k][j] == "#":
                            data[k + 1][j] = "O"
                            if k + 1 != i:
                                data[i][j] = "."
                            break

        rocas_por_fila = []
        for line in data:
            contador = 0
            for char in line:
                if char == "O":
                    contador += 1
            rocas_por_fila.append(contador)

        rocas_por_fila.reverse()
        rocas = [roca * (i + 1) for i, roca in enumerate(rocas_por_fila) if roca != 0]
        return sum(rocas)

    def part2(self, data):
        return
