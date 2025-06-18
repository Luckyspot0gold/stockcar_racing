from avalanche_python import Avax

AVALANCHE_RPC = "https://api.avax.network/ext/bc/C/rpc"

class AvalancheRacing:
    def __init__(self):
        self.avax = Avax(AVALANCHE_RPC)
        self.subnet_id = "Yt9d8RRW9JcoqfvyefqJJMX14HawtBc28J9CQspQKPkdonp1y"
    
    def mint_achievement(self, achievement, wallet):
        metadata = {
            "achievement": achievement,
            "protocol": "Wyoming-7",
            "game": "Crypto Clashers Racing"
        }
        return self.avax.create_nft(
            name=f"Racing Achievement: {achievement}",
            description="Earned in Crypto Clashers Racing",
            metadata=metadata,
            to_address=wallet,
            subnet_id=self.subnet_id
        )
