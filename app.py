cd stockcar_racing
# Apply the market fix if not done
curl -o src/market.py https://gist.githubusercontent.com/dee-stoneverse/3f8c74a2b8f58b7d0b9e6a7/raw/wyoming_market_fix.py

# Create a minimal app.py for deployment
cat <<EOT > app.py
from src.game_engine.core import QuantumRacingEngine
import os

if __name__ == "__main__":
    if os.environ.get('QUANTUM_DEPLOY'):
        # Run in server mode
        from pyngrok import ngrok
        public_url = ngrok.connect(8000)
        print(f"Quantum Racing LIVE at: {public_url}")
    game = QuantumRacingEngine()
    game.run()
EOT

# Install pyngrok for temporary public URL
pip install pyngrok

# Run locally with public URL (for demo purposes)
QUANTUM_DEPLOY=1 python app.py
