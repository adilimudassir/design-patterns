from abc import ABC, abstractmethod

class PhysicalDeliveryProvider(ABC):
    @abstractmethod
    def arrange_delivery(self, amount: float) -> None:
        pass
