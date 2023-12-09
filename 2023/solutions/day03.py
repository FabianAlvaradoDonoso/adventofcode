from utils.solution_base import SolutionBase
import re
from functools import reduce


class Solution(SolutionBase):
    @staticmethod
    def obtener_adyacentes(matriz, fila, columna, posicion=False):
        adyacentes = []

        # Obtener la forma de la matriz
        filas, columnas = len(matriz), len(matriz[0])

        # Función auxiliar para verificar los límites y agregar el elemento adyacente
        def agregar_adyacente(f, c):
            if 0 <= f < filas and 0 <= c < columnas:
                if posicion:
                    adyacentes.append([matriz[f][c], f, c])
                else:
                    adyacentes.append(matriz[f][c])

        # Obtener elementos adyacentes y en las diagonales
        agregar_adyacente(fila - 1, columna - 1)  # Superior izquierda
        agregar_adyacente(fila - 1, columna)  # Superior
        agregar_adyacente(fila - 1, columna + 1)  # Superior derecha
        agregar_adyacente(fila, columna - 1)  # Izquierda
        agregar_adyacente(fila, columna + 1)  # Derecha
        agregar_adyacente(fila + 1, columna - 1)  # Inferior izquierda
        agregar_adyacente(fila + 1, columna)  # Inferior
        agregar_adyacente(fila + 1, columna + 1)  # Inferior derecha

        return adyacentes

    @staticmethod
    def delete_item_from_list(caracter, list, position=False):
        if position:
            return [item for item in list if item[0] != caracter]
        else:
            return [item for item in list if item != caracter]

    @staticmethod
    def delete_item_number_from_list(list):
        return [item for item in list if not re.search(r"\d", item)]

    @staticmethod
    def encontrar_numero(lista, posicion):
        # Verificar si la posición está dentro de los límites de la lista
        if 0 <= posicion < len(lista) and lista[posicion].isdigit():
            # Buscar hacia la izquierda desde la posición dada
            inicio = posicion
            while inicio >= 0 and lista[inicio].isdigit():
                inicio -= 1

            # Buscar hacia la derecha desde la posición dada
            fin = posicion
            while fin < len(lista) and lista[fin].isdigit():
                fin += 1

            # Devolver el número encontrado
            numero_completo = lista[inicio + 1 : fin]
            return numero_completo

        # Si la posición está fuera de los límites o no es un dígito, devolver None
        return None

    @staticmethod
    def multiplicar_lista(lista):
        resultado = reduce(lambda x, y: x * y, lista)
        return resultado

    def part1(self, data):
        # separa cada caracter excepto los numeros y los une en una matriz
        matriz = [
            list(filter(lambda x: x.strip() != "", re.findall(r".", cadena)))
            for cadena in data
        ]

        numeros_por_sumar = []
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                adyacentes = None

                if matriz[i][j].isdigit():
                    adyacentes = Solution.obtener_adyacentes(matriz, i, j)
                    adyacentes = Solution.delete_item_from_list(".", adyacentes)
                    adyacentes = Solution.delete_item_number_from_list(adyacentes)

                if adyacentes:
                    numero_completo = Solution.encontrar_numero(matriz[i], j)
                    numero_completo = int("".join(numero_completo))

                    # si el ultimo numero de numeros_por_sumar es distinto al numero_completo, agregar el numero_completo a la lista
                    if not numeros_por_sumar:
                        numeros_por_sumar.append(numero_completo)

                    if numeros_por_sumar and numeros_por_sumar[-1] != numero_completo:
                        numeros_por_sumar.append(numero_completo)

        return sum(numeros_por_sumar)

    def part2(self, data):
        # separa cada caracter excepto los numeros y los une en una matriz
        matriz = [
            list(filter(lambda x: x.strip() != "", re.findall(r".", cadena)))
            for cadena in data
        ]

        numeros_por_sumar = []
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                numeros_por_multiplicar = []
                adyacentes = None

                if matriz[i][j] == "*":
                    adyacentes = Solution.obtener_adyacentes(
                        matriz, i, j, posicion=True
                    )
                    adyacentes = Solution.delete_item_from_list(
                        ".", adyacentes, position=True
                    )

                if adyacentes:
                    for item in adyacentes:
                        numero_completo = Solution.encontrar_numero(
                            matriz[item[1]], item[2]
                        )
                        numero_completo = int("".join(numero_completo))

                        if not numeros_por_multiplicar:
                            numeros_por_multiplicar.append(numero_completo)

                        if (
                            numeros_por_multiplicar
                            and numeros_por_multiplicar[-1] != numero_completo
                        ):
                            numeros_por_multiplicar.append(numero_completo)

                if numeros_por_multiplicar:
                    if len(numeros_por_multiplicar) > 1:
                        gear_ratio = Solution.multiplicar_lista(numeros_por_multiplicar)
                        numeros_por_sumar.append(gear_ratio)

        return sum(numeros_por_sumar)
