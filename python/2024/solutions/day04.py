from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def search_all_directions(self, data, x, y, items, only_diagonal=False):
        buffer_items = []

        if not only_diagonal:
            # right
            if x + items <= len(data[y]):
                buffer = ""
                for i in range(x, x + items):
                    buffer += data[y][i]
                buffer_items.append([buffer, "right"])

            # left
            if x - items >= -1:
                buffer = ""
                for i in range(x, x - items, -1):
                    buffer += data[y][i]
                buffer_items.append([buffer, "left"])

            # down
            if y + items <= len(data):
                buffer = ""
                for i in range(y, y + items):
                    buffer += data[i][x]
                buffer_items.append([buffer, "down"])

            # up
            if y - items >= -1:
                buffer = ""
                for i in range(y, y - items, -1):
                    buffer += data[i][x]
                buffer_items.append([buffer, "up"])

        # up left
        if y - items >= -1 and x - items >= -1:
            buffer = ""
            for i in range(items):
                buffer += data[y - i][x - i]
            buffer = buffer[1:] if only_diagonal else buffer
            buffer_items.append([buffer, "up left"])

        # down right
        if y + items <= len(data) and x + items <= len(data[y]):
            buffer = ""
            for i in range(items):
                buffer += data[y + i][x + i]
            buffer = buffer[1:] if only_diagonal else buffer
            buffer_items.append([buffer, "down right"])

        # up right
        if y - items >= -1 and x + items <= len(data[y]):
            buffer = ""
            for i in range(items):
                buffer += data[y - i][x + i]
            buffer = buffer[1:] if only_diagonal else buffer
            buffer_items.append([buffer, "up right"])

        # down left
        if x - items >= -1 and y + items <= len(data):
            buffer = ""
            for i in range(items):
                buffer += data[y + i][x - i]
            buffer = buffer[1:] if only_diagonal else buffer
            buffer_items.append([buffer, "down left"])

        return buffer_items

    def part1(self, data):
        data = [list(line) for line in data]
        num_search = 0

        for y in range(len(data)):
            for x in range(len(data[y])):
                if data[y][x] != "X":
                    continue

                items = self.search_all_directions(data=data, x=x, y=y, items=4)

                for item in items:
                    if item[0] == "XMAS":
                        num_search += 1

        return num_search

    def part2(self, data):
        data = [list(line) for line in data]
        num_search = 0

        for y in range(len(data)):
            for x in range(len(data[y])):
                if data[y][x] != "A":
                    continue

                items = self.search_all_directions(data=data, x=x, y=y, items=2, only_diagonal=True)
                if len(items) != 4:  # noqa
                    continue

                item1 = items[0][0] + "A" + items[1][0]
                item2 = items[2][0] + "A" + items[3][0]

                cross1 = False
                if item1 == "MAS" or item1[::-1] == "MAS":
                    cross1 = True

                cross2 = False
                if item2 == "MAS" or item2[::-1] == "MAS":
                    cross2 = True

                if cross1 and cross2:
                    num_search += 1

        return num_search
