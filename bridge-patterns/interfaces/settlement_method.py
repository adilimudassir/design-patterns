from abc import ABC, abstractmethod

class SettlementMethod(ABC):
    @abstractmethod
    def settle(self, amount: float) -> None:
        pass
