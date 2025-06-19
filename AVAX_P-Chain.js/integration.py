# Add at top of file
class AvalancheIntegration:
    def __init__(self):
        self.nfts_minted = 0
        
    def mint_achievement(self, car_name):
        print(f"AVALANCHE: Minting NFT for {car_name} win")
        self.nfts_minted += 1
        return f"AVAX-NFT-{self.nfts_minted}"

# Add after car creation
avax = AvalancheIntegration()

# Add inside win detection
if car.laps >= 3:
    nft_id = avax.mint_achievement(car.name)
    win_text = font.render(f"{car.name} WINS! NFT: {nft_id}", True, (0, 255, 0))
    screen.blit(win_text, (WIDTH//2 - win_text.get_width()//2, HEIGHT//2))
