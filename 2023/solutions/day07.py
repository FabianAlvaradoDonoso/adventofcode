from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    @staticmethod
    def get_type_hand(hand):
        hand = list(hand)
        hand = sorted(hand)
        cards = {}

        for card in hand:
            if card in cards:
                cards[card] += 1
            else:
                cards[card] = 1

        cards = {
            k: v
            for k, v in sorted(cards.items(), key=lambda item: item[1], reverse=True)
        }

        if 5 in cards.values():
            return "five of a kind", 7
        if 4 in cards.values():
            return "four of a kind", 6
        if 3 in cards.values() and 2 in cards.values():
            return "full house", 5
        if 3 in cards.values():
            return "three of a kind", 4
        if list(cards.values()) == [2, 2, 1]:
            return "two pair", 3
        if 2 in cards.values():
            return "one pair", 2
        return "high card", 1

    @staticmethod
    def assign_positions(hands):
        card_values = "AKQJT98765432"

        def compare_hands(hand1, hand2):
            for card1, card2 in zip(hand1["hand"], hand2["hand"]):
                if card_values.index(card1) > card_values.index(card2):
                    return 1
                elif card_values.index(card1) < card_values.index(card2):
                    return -1
            return 0

        # Ordena las manos de mayor a menor
        sorted_hands = sorted(
            hands,
            key=lambda hand: [card_values.index(card) for card in hand["hand"]],
            reverse=True,
        )

        # Asigna la posición a cada mano
        for i, hand in enumerate(sorted_hands, start=1):
            hand["position"] = i

        return sorted_hands

    def part1(self, data):
        games_list = []
        for game in data:
            hand, bid = game.split(" ")
            games_list.append({"hand": hand, "bid": int(bid)})

        for game in games_list:
            hand, bid = game["hand"], game["bid"]
            type_hand, level = Solution.get_type_hand(hand)
            game["type_hand"] = type_hand
            game["level"] = level

        # ordenar games_list por level
        games_list = sorted(games_list, key=lambda k: k["level"], reverse=True)

        # obtener todos los tipos de levels que hay en games_list
        levels = sorted(list(set(game["level"] for game in games_list)), reverse=True)

        hands_per_level = {
            level: Solution.assign_positions(
                [game for game in games_list if game["level"] == level]
            )
            for level in levels
        }

        # ordenar hands_per_level por level ascendente
        hands_per_level = {
            k: v for k, v in sorted(hands_per_level.items(), key=lambda item: item[0])
        }

        # dejar en una lista todos los hands_per_level ordenados por level ascendente y por position ascendente
        hands_per_level_list = [
            hand for hands in hands_per_level.values() for hand in hands
        ]

        total_winning = 0
        for index, hand in enumerate(hands_per_level_list):
            total_winning += hand["bid"] * (index + 1)

        return total_winning

    def part2(self, data):
        dta = []
        for linein in data:
            game_split_1 = linein.split(" ")
            dta.append((game_split_1[0], int(game_split_1[1])))

        def mapper(itm):
            pair, two_pair, three_kind, four_kind, five_kind = (
                False,
                False,
                False,
                False,
                False,
            )

            # First remove jokers, to decide hand without jokers.
            no_jokers = itm.replace("J", "")
            for c in "AKQT98765432":
                cnt = no_jokers.count(c)
                if cnt == 2:
                    pair, two_pair = (False, True) if pair else (True, False)
                if cnt == 3:
                    three_kind = True
                if cnt == 4:
                    four_kind = True
                if cnt == 5:
                    five_kind = True

            # Then add back jokers, enhancing the hand as they are added back
            for i in range(itm.count("J")):
                if four_kind:
                    five_kind, four_kind = True, False
                elif three_kind:
                    four_kind, three_kind = True, False
                elif two_pair:
                    pair, two_pair, three_kind = True, False, True
                elif pair:
                    pair, three_kind = False, True
                else:
                    pair = True

            # Prefix the item, with a letter indicating type of hand, which is sorted first.
            if five_kind:
                key = "Z" + itm  # five of kind
            elif four_kind:
                key = "Y" + itm  # four of kind
            elif three_kind and pair:
                key = "X" + itm  # full house
            elif three_kind:
                key = "W" + itm  # three of kind
            elif two_pair:
                key = "V" + itm  # two pair
            elif pair:
                key = "U" + itm  # one pair
            else:
                key = "T" + itm  # high card

            # replace chars AKQJT, with FED1B, to ensure rest of hand is sorted correctly
            key = (
                key.replace("A", "F")
                .replace("K", "E")
                .replace("Q", "D")
                .replace("J", "1")
                .replace("T", "B")
            )

            return key

        dta.sort(key=lambda itm: mapper(itm[0]))

        i = 0
        total = 0
        for itm in dta:
            i += 1
            total += itm[1] * i

        return total
