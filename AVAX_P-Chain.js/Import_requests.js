import requests

class AvalancheIntegration:
    def __init__(self, backend_url="http://localhost:5000"):
        self.backend_url = backend_url

    def mint_achievement_nft(self, player_address, achievement_id):
        response = requests.post(
            f"{self.backend_url}/mint",
            json={
                "player_address": player_address,
                "achievement_id": achievement_id
            }
        )
        if response.status_code == 200:
            return response.json()['tx_hash']
        else:
            raise Exception(f"Minting failed: {response.text}")
