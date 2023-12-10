from utils.solution_base import SolutionBase
import re


class Solution(SolutionBase):
    def obtener_adyacentes(self, matrix, fila, columna):
        adyacentes = []

        # Definir las direcciones posibles (arriba, abajo, izquierda, derecha)
        direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        item_actual = matrix[fila][columna]

        for dx, dy in direcciones:
            nueva_fila, nueva_columna = fila + dx, columna + dy

            # Verificar si la nueva posición está dentro de los límites de la matriz
            if 0 <= nueva_fila < len(matrix) and 0 <= nueva_columna < len(matrix[0]):
                item = matrix[nueva_fila][nueva_columna]

                # Verificar las reglas para los adyacentes considerando el item actual
                if (
                    (
                        item_actual == "F"
                        and (
                            (item in ("J", "7", "-") and dy == 1)
                            or (item in ("J", "L", "|") and dx == 1)
                        )
                    )
                    or (
                        item_actual == "J"
                        and (
                            (item in ("F", "L", "-") and dy == -1)
                            or (item in ("F", "7", "|") and dx == -1)
                        )
                    )
                    or (
                        item_actual == "L"
                        and (
                            (item in ("J", "7", "-") and dy == 1)
                            or (item in ("F", "7", "|") and dx == -1)
                        )
                    )
                    or (
                        item_actual == "7"
                        and (
                            (item in ("F", "L", "-") and dy == -1)
                            or (item in ("J", "L", "|") and dx == 1)
                        )
                    )
                    or (
                        item_actual == "-"
                        and (
                            (item in ("J", "7", "-") and dy == 1)
                            or (item in ("F", "L", "-") and dy == -1)
                        )
                    )
                    or (
                        item_actual == "|"
                        and (
                            (item in ("J", "L", "|") and dx == 1)
                            or (item in ("F", "7", "|") and dx == -1)
                        )
                    )
                    or (
                        item_actual == "S"
                        and (
                            (item in ("J", "L", "|") and dx == 1)
                            or (item in ("F", "7", "|") and dx == -1)
                            or (item in ("J", "7", "-") and dy == 1)
                            or (item in ("F", "L", "-") and dy == -1)
                        )
                    )
                ):
                    adyacentes.append([item, nueva_fila, nueva_columna])

        return adyacentes

    def part1(self, data):
        matrix = [list(line) for line in data]

        # Buscar la posición de 'S'
        for fila_inicial, row in enumerate(matrix):
            if "S" in row:
                columna_inicial = row.index("S")
                break

        inicial_1, inicial_2 = self.obtener_adyacentes(
            matrix, fila_inicial, columna_inicial
        )

        fila_anterior_1, columna_anterior_1 = fila_inicial, columna_inicial
        fila_anterior_2, columna_anterior_2 = fila_inicial, columna_inicial

        pasos = 2
        while True:
            adyacentes_1 = self.obtener_adyacentes(matrix, inicial_1[1], inicial_1[2])
            for adyacente in adyacentes_1:
                if (adyacente[1], adyacente[2]) != (
                    fila_anterior_1,
                    columna_anterior_1,
                ):
                    fila_anterior_1, columna_anterior_1 = inicial_1[1], inicial_1[2]
                    inicial_1 = adyacente
                    break

            adyacentes_2 = self.obtener_adyacentes(matrix, inicial_2[1], inicial_2[2])
            for adyacente in adyacentes_2:
                if (adyacente[1], adyacente[2]) != (
                    fila_anterior_2,
                    columna_anterior_2,
                ):
                    fila_anterior_2, columna_anterior_2 = inicial_2[1], inicial_2[2]
                    inicial_2 = adyacente
                    break

            if (inicial_1[1], inicial_1[2]) == (inicial_2[1], inicial_2[2]):
                break
            pasos += 1

        return pasos

    # Code thief 😅

    def parse_map(self, data):
        start = None
        _map = []

        for h, line in enumerate(data):
            _map.append(list(line))
            if "S" in line:
                start = (h, line.index("S"))

        """ four adjacent directions """
        adj_dirs = [  # top, right, bottom, left
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1),
        ]

        """ define the direction connected to the adjacent node for each symbol """
        symbol_connects = {  # top, right, bottom, left
            "|": (1, 0, 1, 0),
            "-": (0, 1, 0, 1),
            "L": (1, 1, 0, 0),
            "J": (1, 0, 0, 1),
            "7": (0, 0, 1, 1),
            "F": (0, 1, 1, 0),
        }

        """ define the types of adjacent nodes that can be connected for each direction """
        # adj_connect_types = {pos: [k for k, v in symbol_connects.items() if v[(i + 2) % 4]] for i, pos in enumerate(adj_dirs)}
        adj_connect_types = {
            (-1, 0): "F|7",
            (0, 1): "7-J",
            (1, 0): "L|J",
            (0, -1): "F-L",
        }

        adjs = [0, 0, 0, 0]  # top, right, bottom, left
        for i, adj in enumerate(adj_dirs):
            pos = tuple(a + b for a, b in zip(start, adj))
            if _map[pos[0]][pos[1]] in adj_connect_types[adj]:
                adjs[i] = 1

        _map[start[0]][start[1]] = {v: k for k, v in symbol_connects.items()}[
            tuple(adjs)
        ]

        queue = [start]
        visited = set()

        while queue:
            pos = queue.pop(0)
            if pos in visited:
                continue
            visited.add(pos)
            if _map[pos[0]][pos[1]] in " .":
                continue

            sym = _map[pos[0]][pos[1]]
            _dirs = [adj_dirs[i] for i, v in enumerate(symbol_connects[sym]) if v == 1]
            for dy, dx in _dirs:
                queue.append((pos[0] + dy, pos[1] + dx))

        return _map, start, visited

    def part2(self, data):
        _map, _start, _loop_nodes = self.parse_map(data)
        row_counts = []

        for h, items in enumerate(_map):
            line = [v if (h, w) in _loop_nodes else "." for w, v in enumerate(items)]
            line = "".join(line)

            line = re.sub(r"L-*7", "|", line)
            line = re.sub(r"L-*J", "||", line)
            line = re.sub(r"F-*7", "||", line)
            line = re.sub(r"F-*J", "|", line)

            cross = 0
            inside = 0

            for c in line:
                if c == "." and cross % 2:
                    inside += 1
                elif c in "F7LJ|":
                    cross += 1
            row_counts.append(inside)
        return sum(row_counts)
