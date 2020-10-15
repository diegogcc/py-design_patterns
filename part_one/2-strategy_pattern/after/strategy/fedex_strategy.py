from strategy.strategy_abc import ABCStrategy

class FedexStrategy(ABCStrategy):
    
    def calculate(self, order):
        return 3.00