sequenceDiagram
    participant Game
    participant QuantumSigner
    participant Avalanche
    participant PlayerWallet
    
    Game->>QuantumSigner: Sign achievement data
    QuantumSigner-->>Game: Quantum signature
    Game->>Avalanche: Mint NFT (with signature)
    Avalanche-->>Game: Transaction hash
    Game->>PlayerWallet: Send NFT notification
