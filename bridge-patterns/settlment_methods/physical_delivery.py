from interfaces.settlement_method import SettlementMethod
from interfaces.physical_delivery_provider import PhysicalDeliveryProvider
class PhysicalDelivery(SettlementMethod):
    def __init__(self, provider: PhysicalDeliveryProvider):
        self.provider = provider

    def settle(self, amount: float) -> None:
        self.provider.arrange_delivery(amount)