from abc import ABC, abstractmethod

class CashSettlementProvider(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> None:
        pass
