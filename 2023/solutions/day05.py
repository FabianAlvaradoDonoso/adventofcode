from utils.solution_base import SolutionBase
import math


class Solution(SolutionBase):
    @staticmethod
    def ordenar_info(info):
        maps_dict = {}
        current_map = []
        current_map_key = None

        for line in info:
            if "map" in line:
                if current_map_key and current_map:
                    maps_dict[current_map_key] = current_map
                    current_map = []
                current_map_key = line.strip(":")
            elif "seeds" in line:
                seeds_line = line.split(":")
                if len(seeds_line) == 2:
                    seeds_key = seeds_line[0].strip()
                    seeds_values = list(map(int, seeds_line[1].split()))
                    maps_dict[seeds_key] = seeds_values
            elif current_map_key:
                current_map.append(list(map(int, line.split())))

        # Asegurarse de agregar el último map
        if current_map_key and current_map:
            maps_dict[current_map_key] = current_map

        return maps_dict

    @staticmethod
    def get_next_step(info_map, step_origen, print_debug=False):
        step_destino = None
        for info in info_map:
            if len(info) == 0:
                continue
            destino, origen, rango = info
            rango_origen = [0, 0 + rango]

            if (
                step_origen >= rango_origen[0] + origen
                and step_origen < rango_origen[1] + origen
            ):
                delta_index = step_origen - origen
                step_destino = delta_index + destino
        if not step_destino:
            step_destino = step_origen

        return step_destino

    def part1(self, data):
        info = Solution.ordenar_info(data)

        seeds = info["seeds"]
        locations = math.inf

        for seed in seeds:
            step = seed
            for mapping in info.keys():
                if "map" in mapping:
                    step = Solution.get_next_step(info[mapping], step)
            locations = min(locations, step)

        return locations

    def part2(self, data):
        seeds_line = data[0]
        seeds = [int(x) for x in seeds_line.split(":")[1].split(" ") if x]

        mappings = []

        new_mapping = False
        mapping = None
        for line in data[1:]:
            if not line:
                new_mapping = True
            elif new_mapping:
                new_mapping = False
                mappings.append([])
            else:
                [dest, source, range] = [int(x) for x in line.split(" ")]
                mappings[-1].append((source, dest, range))

        for mapping in mappings:
            mapping.sort()

        seed_start = None
        ranges = []
        for i, seed_number in enumerate(seeds):
            if i % 2 == 0:
                seed_start = seed_number
            else:
                ranges.append((seed_start, seed_start + seed_number - 1))

        ranges.sort()

        for iteration, mapping in enumerate(mappings):
            i = 0
            j = 0
            new_ranges = []

            range = None
            while ranges or range:
                if not range:
                    range = ranges.pop(0)

                range_start = range[0]
                range_end = range[1]

                if j >= len(mapping):
                    new_ranges.append((range_start, range_end))
                    range = None
                    i += 1
                    continue

                mapping_start = mapping[j][0]
                mapping_end = mapping[j][0] + mapping[j][2] - 1

                mapping_shift = mapping[j][1] - mapping[j][0]

                if range_start < mapping_start and range_end < mapping_start:
                    new_ranges.append((range_start, range_end))
                    range = None
                    i += 1
                elif range_start >= mapping_start and range_end <= mapping_end:
                    new_ranges.append(
                        (range_start + mapping_shift, range_end + mapping_shift)
                    )
                    range = None
                    i += 1
                elif range_start <= mapping_start and range_end <= mapping_end:
                    if range_start < mapping_start:
                        new_ranges.append((range_start, mapping_start - 1))
                    new_ranges.append(
                        (mapping_start + mapping_shift, range_end + mapping_shift)
                    )
                    range = None
                    i += 1
                elif range_start <= mapping_start and range_end >= mapping_end:
                    if range_start < mapping_start:
                        new_ranges.append((range_start, mapping_start - 1))
                    new_ranges.append(
                        (mapping_start + mapping_shift, mapping_end + mapping_shift)
                    )
                    if range_end > mapping_end:
                        ranges = [(mapping_end + 1, range_end)] + ranges
                    range = None
                elif range_start <= mapping_end and range_end > mapping_end:
                    new_ranges.append(
                        (range_start + mapping_shift, mapping_end + mapping_shift)
                    )
                    ranges = [(mapping_end + 1, range_end)] + ranges
                    range = None
                else:
                    j += 1

            ranges = new_ranges
            ranges.sort()

        return min(ranges)[0]
