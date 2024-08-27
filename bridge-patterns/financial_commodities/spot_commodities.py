from interfaces.financial_commodity import FinancialCommodity
from interfaces.settlement_method import SettlementMethod

class SpotCommodities(FinancialCommodity):
    
    def __init__(self, settlement_method: SettlementMethod):
        self.settlement_method = settlement_method
    
    def process(self, amount: float) -> None:
        print("Processing spot commodities contract...")
        self.settlement_method.settle(amount)