from unittest.mock import MagicMock
from adapters.prembly import PremblyAdapter
from adapters.qore_id import QoreIDAdapter
from adapters.verify_me import VerifyMeAdapter
from identify_provider import IdentityProvider

if __name__ == '__main__':
    # Instantiate clients
    qoreid_client = MagicMock()
    verifyme_client = MagicMock()
    prembly_client = MagicMock()

    # Create adapters using the clients
    qoreid_adapter = QoreIDAdapter(qoreid_client=qoreid_client)
    verifyme_adapter = VerifyMeAdapter(verifyme_client=verifyme_client)
    prembly_adapter = PremblyAdapter(prembly_client=prembly_client)

    # Create identity providers using the adapters
    qoreid_verifier = IdentityProvider(adapter=qoreid_adapter)
    verifyme_verifier = IdentityProvider(adapter=verifyme_adapter)
    prembly_verifier = IdentityProvider(adapter=prembly_adapter)

    # Sample verification calls
    print("QoreID Verification:")
    print(f"Driver License DL12345: {qoreid_verifier.verify_driver_license(license_number='DL12345')}")
    print(f"NIN NIN12345: {qoreid_verifier.verify_nin(nin='NIN12345')}")
    print(f"BVN BVN12345: {qoreid_verifier.verify_bvn(bvn='BVN12345')}")

    print("\nVerifyMe Verification:")
    print(f"Driver License DL12345: {verifyme_verifier.verify_driver_license(license_number='DL12345')}")
    print(f"NIN NIN12345: {verifyme_verifier.verify_nin(nin='NIN12345')}")
    print(f"BVN BVN12345: {verifyme_verifier.verify_bvn(bvn='BVN12345')}")

    print("\nPrembly Verification:")
    print(f"Driver License DL12345: {prembly_verifier.verify_driver_license(license_number='DL12345')}")
    print(f"NIN NIN12345: {prembly_verifier.verify_nin(nin='NIN12345')}")
    print(f"BVN BVN12345: {prembly_verifier.verify_bvn(bvn='BVN12345')}")