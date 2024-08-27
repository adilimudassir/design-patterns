from interfaces.adapter import IdentityProviderAdapter


class IdentityProvider():
    def __init__(self, adapter: IdentityProviderAdapter):
        self.adapter = adapter

    def verify_driver_license(self, license_number: str) -> bool:
        return self.adapter.verify_driver_license(license_number=license_number)

    def verify_nin(self, nin: str) -> bool:
        return self.adapter.verify_nin(nin=nin)

    def verify_bvn(self, bvn: str) -> bool:
        return self.adapter.verify_bvn(bvn=bvn)
