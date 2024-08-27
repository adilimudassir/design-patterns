from abc import ABC, abstractmethod

class FinancialCommodity(ABC):
    @abstractmethod
    def process(self, amount: float) -> None:
        pass
