// contracts/CoinOnboarding.sol
function listCoin(string memory coinSymbol, uint tier) public payable {
  require(msg.value == tierPrices[tier], "Incorrect payment");
  require(!coinListed[coinSymbol], "Already listed");
  coinListed[coinSymbol] = true;
  emit NewListing(coinSymbol, tier, msg.sender);
}
