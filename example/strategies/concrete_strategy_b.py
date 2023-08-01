from typing import List

from strategy import Strategy


class ConcreteStrategy(Strategy):
    def do_algorithm(self, data: List) -> List:
        return reversed(sorted(data))