import math
import sys


def ordenar_info(info):
    maps_dict = {}
    current_map = []
    current_map_key = None

    for line in content:
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


def get_next_step(info_map, step_origen, print_debug=False):
    step_destino = None
    for info in info_map:
        destino, origen, rango = info
        rango_origen = [0, 0 + rango]
        rango_destino = [0, 0 + rango]

        if (
            step_origen >= rango_origen[0] + origen
            and step_origen < rango_origen[1] + origen
        ):
            delta_index = step_origen - origen
            step_destino = delta_index + destino
    if not step_destino:
        step_destino = step_origen

    return step_destino


# ---- PART ONE ---- #

with open("input_5.txt") as f:
    content = f.readlines()
content = [x.replace("\n", "") for x in content if x != "\n"]

info = ordenar_info(content)

seeds = info["seeds"]
locations = math.inf

for seed in seeds:
    step = seed
    for mapping in info.keys():
        if "map" in mapping:
            step = get_next_step(info[mapping], step)
    locations = min(locations, step)

print("Result:", locations)
