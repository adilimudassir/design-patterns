from interfaces.adapter import IdentityProviderAdapter


class PremblyAdapter(IdentityProviderAdapter):
    def __init__(self, prembly_client):
        self.prembly_client = prembly_client

    def verify_driver_license(self, license_number: str) -> bool:
        response = self.prembly_client.validate_license(license_number)
        return response['verification_status'] == 'success'

    def verify_nin(self, nin: str) -> bool:
        response = self.prembly_client.validate_nin(nin)
        return response['verification_status'] == 'success'

    def verify_bvn(self, bvn: str) -> bool:
        response = self.prembly_client.validate_bvn(bvn)
        return response['verification_status'] == 'success'
