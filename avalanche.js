// src/blockchain/avalanche.js
import { Avalanche } from "@avalabs/avalanchejs"

const avalanche = new Avalanche(
  "127.0.0.1", 
  60172,
  "ext/bc/Yt9d8RRW9JcoqfvyefqJJMX14HawtBc28J9CQspQKPkdonp1y/rpc",
  888,
  "TST"
)

export const placeBet = async (raceId, amount) => {
  const tx = await avalanche.issueTx({
    from: wallet.address,
    to: "0x8db97C7cEcE249c2b98bDC0226Cc4C2A57BF52FC", // House address
    value: amount,
    data: `bet:${raceId}`
  })
  return tx.hash
}
// src/components/WalletConnect.jsx
<button onClick={connectAvalanche} className="avalanche-connect">
  <img src="avalanche-logo.png" alt="Avalanche" />
  Connect Racer Wallet
</button>
