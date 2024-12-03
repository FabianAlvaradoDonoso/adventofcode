from utils.solution_base import SolutionBase
import re

# A - X Rock => 1
# B - Y Paper => 2
# C - Z Scissors => 3

# Lose => 0 points
# Tie => 3 point
# Win => 6 points


class Solution(SolutionBase):
    types_1 = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors",
    }
    types_2 = {
        "X": "lose",
        "Y": "draw",
        "Z": "win",
    }

    points_hand = {"rock": 1, "paper": 2, "scissors": 3}

    def wins(self, enemy, player):
        if enemy == "rock" and player == "paper":
            return 6
        elif enemy == "paper" and player == "scissors":
            return 6
        elif enemy == "scissors" and player == "rock":
            return 6
        elif enemy == player:
            return 3
        else:
            return 0

    def strategy(self, enemy, strategy):
        if strategy == "lose":
            if enemy == "rock":
                return "scissors"
            elif enemy == "paper":
                return "rock"
            elif enemy == "scissors":
                return "paper"
        elif strategy == "draw":
            if enemy == "rock":
                return "rock"
            elif enemy == "paper":
                return "paper"
            elif enemy == "scissors":
                return "scissors"
        elif strategy == "win":
            if enemy == "rock":
                return "paper"
            elif enemy == "paper":
                return "scissors"
            elif enemy == "scissors":
                return "rock"

    def part1(self, data):
        points = 0
        for game in data:
            [enemy, player] = game.split(" ")
            enemy = self.types_1[enemy]
            player = self.types_1[player]
            points += self.wins(enemy, player)
            points += self.points_hand[player]

        return points

    def part2(self, data):
        points = 0
        for game in data:
            [enemy, strategy] = game.split(" ")
            enemy = self.types_1[enemy]
            strategy = self.types_2[strategy]

            player = self.strategy(enemy, strategy)

            points += self.wins(enemy, player)
            points += self.points_hand[player]

        return points
