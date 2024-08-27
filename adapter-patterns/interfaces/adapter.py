from abc import ABC, abstractmethod

class IdentityProviderAdapter(ABC):
    @abstractmethod
    def verify_driver_license(self, license_number: str) -> bool:
        pass

    @abstractmethod
    def verify_nin(self, nin: str) -> bool:
        pass

    @abstractmethod
    def verify_bvn(self, bvn: str) -> bool:
        pass
