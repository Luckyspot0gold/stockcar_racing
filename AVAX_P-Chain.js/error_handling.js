try:
    tx_hash = quantum_signed_mint(wallet, "FirstWin")
except Exception as e:
    # Wyoming Protocol 7 fallback
    store_locally({
        "achievement": "FirstWin",
        "player": wallet,
        "retry_after": time.time() + 3600  # 1 hour
    })
