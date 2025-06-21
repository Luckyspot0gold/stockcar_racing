Avalanche Integration Snippet** (Save as `avax.js`):  
```javascript
import { Bolt } from '@bolt-io/sdk'; 
const bolt = new Bolt(process.env.BOLT_API_KEY);
// Mint testnet tokens for player
async function mintPlayerTokens(playerWallet) {
  return await bolt.avax.mintTestTokens(playerWallet, 1000); // 1000 $TEST
}
