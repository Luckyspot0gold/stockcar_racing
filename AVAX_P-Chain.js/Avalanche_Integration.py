import json
import os
from web3 import Web3
from web3.middleware import geth_poa_middleware

class AvalancheIntegration:
    def __init__(self, network_url="https://api.avax-test.network/ext/bc/C/rpc"):
        self.w3 = Web3(Web3.HTTPProvider(network_url))
        # Inject PoA middleware for Avalanche
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        self.contract_address = None
        self.contract_abi = None
        self.contract = None

    def load_contract(self, contract_address, abi_path):
        self.contract_address = contract_address
        with open(abi_path) as f:
            self.contract_abi = json.load(f)
        self.contract = self.w3.eth.contract(address=contract_address, abi=self.contract_abi)

    def mint_achievement_nft(self, private_key, to_address, token_uri):
        if not self.contract:
            raise Exception("Contract not loaded")

        account = self.w3.eth.account.privateKeyToAccount(private_key)
        nonce = self.w3.eth.get_transaction_count(account.address)

        # Build transaction
        tx = self.contract.functions.mint(to_address, token_uri).build_transaction({
            'chainId': 43113,  # Avalanche Fuji testnet
            'gas': 2000000,
            'gasPrice': self.w3.toWei('25', 'gwei'),
            'nonce': nonce,
        })

        # Sign and send
        signed_tx = account.sign_transaction(tx)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return tx_hash.hex()
        from stone_sdk import QuantumSigner

def quantum_signed_mint(player_wallet, achievement):
    # Generate quantum-proof signature
    signer = QuantumSigner(protocol="Wyoming-7")
    message = f"MINT:{achievement}:{player_wallet}"
    signature = signer.sign(message)
    
    # Include signature in metadata
    metadata["quantum_proof"] = signature
    
    return avax.create_nft(..., metadata=metadata)

# Example usage:
# avalanche = AvalancheIntegration()
# avalanche.load_contract("0x...", "path/to/abi.json")
# tx_hash = avalanche.mint_achievement_nft(private_key, player_address, "https://example.com/nft_metadata.json")
