# Secure wallet connection:
def connect_wallet():
    if 'ethereum' in window:
        accounts = window.ethereum.request({method: 'eth_requestAccounts'})
        return accounts[0]
    else:
        raise Exception("Wallet not detected! Install MetaMask")
