# Proper achievement minting:
def mint_race_achievement(player_wallet, achievement_type):
    metadata = {
        "game": "Crypto Clashers Racing",
        "achievement": achievement_type,
        "protocol": "Wyoming-7",
        "date": datetime.now().isoformat()
    }
    
    return avax.create_nft(
        name=f"Racing Achievement: {achievement_type}",
        description=f"Unlocked in Crypto Clashers Racing",
        metadata=metadata,
        to_address=player_wallet
    )
gas_estimate = avax.estimate_gas()
if gas_estimate > 0.1:  # 0.1 AVAX
    raise Exception("Gas fees too high! Try later")
