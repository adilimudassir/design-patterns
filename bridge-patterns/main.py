from providers.mobile_wallet import MobileWallet
from settlment_methods.cash_settlement import CashSettlement
from financial_commodities.spot_commodities import SpotCommodities

from settlment_methods.physical_delivery import PhysicalDelivery
from financial_commodities.deliverable_commodities import DeliverableCommodities
from financial_commodities.otc import OTC
from providers.bank_transfer import BankTransfer
from providers.logistics_service import LogisticsService
from providers.warehouse_pickup import WarehousePickup

if __name__ == "__main__":
    # Cash Settlement using Mobile Wallet
    mobile_wallet = MobileWallet()
    cash_settlement = CashSettlement(provider=mobile_wallet)
    sport_commodities = SpotCommodities(settlement_method=cash_settlement)
    sport_commodities.process(amount=1000000)

    # Deliverable Commodities with Physical Delivery via Logistics Service
    logistics_service = LogisticsService()
    physical_delivery = PhysicalDelivery(provider=logistics_service)
    deliverable_commodities = DeliverableCommodities(settlement_method=physical_delivery)
    deliverable_commodities.process(amount=500000)

    # OTC contract with Cash Settlement via Bank Transfer
    bank_transfer = BankTransfer()
    cash_settlement_bank = CashSettlement(provider=bank_transfer)
    otc_contracts = OTC(settlement_method=cash_settlement_bank)
    otc_contracts.process(amount=2000000)

    # Client Pickup at Warehouse for Deliverable Commodities
    warehouse_pickup = WarehousePickup()
    physical_delivery_warehouse = PhysicalDelivery(provider=warehouse_pickup)
    deliverable_commodities_warehouse = DeliverableCommodities(settlement_method=physical_delivery_warehouse)
    deliverable_commodities_warehouse.process(amount=500000)
