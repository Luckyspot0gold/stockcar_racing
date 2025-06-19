import { ethers } from 'ethers';

const RPC_URL = "http://127.0.0.1:60172/ext/bc/Yt9d8RRW9JcoqfvyefqJJMX14HawtBc28J9CQspQKPkdonp1y/rpc";
const CHAIN_ID = 888;
const HOUSE_ADDRESS = "0x8db97C7cEcE249c2b98bDC0226Cc4C2A57BF52FC"; // using the funded account as the house

function WalletButton() {
  const [account, setAccount] = useState("");
  const [balance, setBalance] = useState("");

  const connectWallet = async () => {
    if (window.ethereum) {
      try {
        // Add the network
        await window.Ethereum.request({
          method: 'wallet_addEthereumChain',
          params: [{
            chainId: `0x${CHAIN_ID.toString(16)}`,
            chainName: 'myblockchain',
            nativeCurrency: {
              name: 'TST Token',
              symbol: 'TST',
              decimals: 18
            },
            rpcUrls: [RPC_URL],
            blockExplorerUrls: []
          }]
        });

        // Request accounts
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        setAccount(accounts[0]);

        // Get balance
        const provider = new ethers.providers.JsonRpcProvider(RPC_URL);
        const balanceWei = await provider.getBalance(accounts[0]);
        setBalance(ethers.utils.formatEther(balanceWei));
      } catch (error) {
        console.error(error);
      }
    } else {
      alert("Please install MetaMask!");
    }
  };

  const placeBet = async () => {
    if (!account) {
      alert("Connect wallet first");
      return;
    }

    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner();

    const tx = await signer.sendTransaction({
      to: HOUSE_ADDRESS,
      value: ethers.utils.parseEther("1") // 1 TST
    });

    alert(`Bet placed! TX: ${tx.hash}`);
  };

  return (
    <div>
      {! Account ? (
        <button onClick={connectWallet}>Connect Wallet</button>
      ) : (
        <div>
          <p>Account: {account}</p>
          <p>Balance: {balance} TST</p>
          <button onClick={placeBet}>Place 1 TST Bet</button>
        </div>
      )}
    </div>
  );
}
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
npm run test-race --coin=BTC --indicator=HollowCandle
npm run dev
// REPLACE FUNCTION AT LINE 112
function claimRewards() public {
    require(rewards[msg.sender] > 0, "No rewards");
    
    // FIXED REENTRANCY PROTECTION
    uint amount = rewards[msg.sender];
    rewards[msg.sender] = 0;  // Reset BEFORE transfer
    
    (bool success, ) = payable(msg.sender).call{value: amount}("");
    require(success, "Transfer failed");
}
npx hardhat run scripts/deployBattle.js --network avalanche
