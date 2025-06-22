import { connectAvalanche } from './emergency-connector.js';

async function initApp() {
  try {
    await connectAvalanche();
    
    // Connect to wallet
    const wallet = await window.avalanche.connect();
    console.log(`Connected address: ${wallet.address}`);
    
    // Mint emergency NFT
    const txHash = window.avalanche.mintNFT({
      name: "Emergency NFT",
      description: "Created during service outage"
    });
    console.log(`Transaction hash: ${txHash}`);
    
  } catch (error) {
    console.error("Avalanche connection failed:", error);
    // Fallback to secondary blockchain
  }
}
