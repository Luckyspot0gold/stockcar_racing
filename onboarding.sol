// contracts/CoinOnboarding.sol
function listCoin(string memory coinSymbol, uint tier) public payable {
  require(msg.value == tierPrices[tier], "Incorrect payment");
  require(!coinListed[coinSymbol], "Already listed");
  coinListed[coinSymbol] = true;
  emit NewListing(coinSymbol, tier, msg.sender);
}
/ REPLACE:
function claimRewards() public {
-   payable(msg.sender).transfer(rewards[msg.sender]);
+   uint amount = rewards[msg.sender];
+   rewards[msg.sender] = 0;
+   payable(msg.sender).transfer(amount); // FIXED REENTRANCY
}
