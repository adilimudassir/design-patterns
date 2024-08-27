from interfaces.adapter import IdentityProviderAdapter


class VerifyMeAdapter(IdentityProviderAdapter):
    def __init__(self, verifyme_client):
        self.verifyme_client = verifyme_client

    def verify_driver_license(self, license_number: str) -> bool:
        response = self.verifyme_client.check_license(license_number)
        return response['is_valid']

    def verify_nin(self, nin: str) -> bool:
        response = self.verifyme_client.check_nin(nin)
        return response['is_valid']

    def verify_bvn(self, bvn: str) -> bool:
        response = self.verifyme_client.check_bvn(bvn)
        return response['is_valid']
