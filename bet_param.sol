function placeBet(uint raceId, address carContract) public payable {
  require(msg.value > 0, "Bet too small");
  bets[raceId][msg.sender] = Bet({
    car: carContract,
    amount: msg.value,
    claimed: false
  });
  totalPrize[raceId] += msg.value;
}
// contracts/RaceBetting.sol
function placeBet(uint raceId, uint carId) public payable {
  require(msg.value > 0, "Bet too small");
  bets[raceId][msg.sender] = Bet({
    car: carId,
    amount: msg.value,
    claimed: false
  });
  totalPrize[raceId] += msg.value;
}
// 5% house fee on all wagers
const calculateWinnings = (betAmount, totalPool) => {
  const houseFee = betAmount * 0.05
  return (betAmount - houseFee) + (totalPool * (betAmount / totalPool))
}
function listCar(string memory coinSymbol, uint tier) public payable {
  require(msg.value == tierPrices[tier], "Incorrect payment");
  cars[coinSymbol] = Car(coinSymbol, tier, true);
}
curl -X POST http://127.0.0.1:60172/ext/bc/Yt9d8RRW9JcoqfvyefqJJMX14HawtBc28J9CQspQKPkdonp1y/rpc \
-d '{"jsonrpc 2.0", "id":1, "method": "eth_getBalance", "params": ["0x8db97C7cEcE249c2b98bDC0226Cc4C2A57BF52FC", "latest"]}'
