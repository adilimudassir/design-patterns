from interfaces.adapter import IdentityProviderAdapter


class QoreIDAdapter(IdentityProviderAdapter):
    def __init__(self, qoreid_client):
        self.qoreid_client = qoreid_client

    def verify_driver_license(self, license_number: str) -> bool:
        response = self.qoreid_client.verify_license(license_number)
        return response['status'] == 'verified'

    def verify_nin(self, nin: str) -> bool:
        response = self.qoreid_client.verify_nin(nin)
        return response['status'] == 'verified'

    def verify_bvn(self, bvn: str) -> bool:
        response = self.qoreid_client.verify_bvn(bvn)
        return response['status'] == 'verified'
