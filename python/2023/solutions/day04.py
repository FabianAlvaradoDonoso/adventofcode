from utils.solution_base import SolutionBase
import re


class Solution(SolutionBase):
    @staticmethod
    def delete_empty_items(list):
        return [item for item in list if item != ""]

    def part1(self, data):
        sum = 0
        for card in data:
            card = card.split(": ")[1]
            winner, numbers_have = card.split(" | ")

            winner = Solution.delete_empty_items([w.strip() for w in winner.split(" ")])
            numbers_have = Solution.delete_empty_items(
                [nh.strip() for nh in numbers_have.split(" ")]
            )

            match = [nh for nh in numbers_have if nh in winner]
            sum += 2 ** (len(match) - 1) if len(match) > 0 else 0

        return sum

    def part2(self, data):
        cards = []
        for card_item in data:
            index_card, num_card = card_item.split(": ")
            winner, numbers_have = num_card.split(" | ")

            index_card = "".join(re.findall(r"\d+", index_card))
            winner = Solution.delete_empty_items([w.strip() for w in winner.split(" ")])
            numbers_have = Solution.delete_empty_items(
                [nh.strip() for nh in numbers_have.split(" ")]
            )

            count_match = len([nh for nh in numbers_have if nh in winner])

            card = {"num": index_card, "match": count_match, "copy": 0}
            cards.append(card)

        for index, card in enumerate(cards):
            if card["match"] > 0:
                increment = card["copy"] + 1
                for i in range(1, card["match"] + 1):
                    if index + i < len(
                        cards
                    ):  # Asegura que no se excedan los límites de la lista
                        cards[index + i]["copy"] += increment
            card["copy"] += 1

        cards_copy = [card["copy"] for card in cards]

        sum = 0
        for card in cards_copy:
            sum += card

        return sum
