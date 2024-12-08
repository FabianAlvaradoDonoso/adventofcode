from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def rules(self, data):
        rules = {}
        for line in data:
            if line == "":
                break

            rule, value = line.split("|")
            previus_values = rules[rule] if rule in rules else []
            previus_values.append(value)
            rules[rule] = previus_values

        return rules

    def updates(self, data):
        updates = []
        for line in data:
            if "|" not in line and line != "":
                update = line.split(",")
                updates.append(update)

        return updates

    def check_order(self, rules, update):
        flag = True
        for i in range(len(update)):
            before = update[:i]
            before_check = all([update[i] in rules[b] for b in before if b in rules])

            after = update[i + 1 :]  # noqa
            after_check = all([a in rules.get(update[i], []) for a in after])

            if not before_check or not after_check:
                flag = False
                break

        return flag

    def part1(self, data):
        rules = self.rules(data)
        updates = self.updates(data)

        check_updates = []
        for u, update in enumerate(updates):
            if self.check_order(rules, update):
                check_updates.append(update)

        central_items = [update[len(update) // 2] for update in check_updates]
        return sum([int(item) for item in central_items])

    def part2(self, data):
        rules = self.rules(data)
        updates = self.updates(data)

        check_updates = []
        for u, update in enumerate(updates):
            if not self.check_order(rules, update):
                check_updates.append(update)

        for u, update in enumerate(check_updates):
            while True:
                if self.check_order(rules, update):
                    break

                for i in range(len(update)):
                    element = update[i]
                    next_element = update[i + 1] if i + 1 < len(update) else None
                    rule_next_element = rules.get(next_element, [])

                    if element in rule_next_element:
                        update[i] = next_element
                        update[i + 1] = element

        central_items = [update[len(update) // 2] for update in check_updates]
        return sum([int(item) for item in central_items])
