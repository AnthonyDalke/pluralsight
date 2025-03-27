from strategy_abc import AbsStrategy


class USPSStrategy(AbsStrategy):
    def calculate(self, order):
        return 5.00
