from interfaces.settlement_method import SettlementMethod
from interfaces.cash_settlement_provider import CashSettlementProvider

class CashSettlement(SettlementMethod):
    def __init__(self, provider: CashSettlementProvider):
        
        self.provider = provider

    def settle(self, amount: float) -> None:
        self.provider.process_payment(amount)

