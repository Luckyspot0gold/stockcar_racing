module.exports = [
  "0xAVAX_Wallet",   // ownerAddress
  15,                // commissionRate (in %)
  "WyoversePortable" // contractName
];
# Frontier Trader commission flow
node utils/enableRoyalties.js --rate 7.5%

# Crypto Clashers tournament entry fees
npx hardhat run scripts/enableTournaments.js
