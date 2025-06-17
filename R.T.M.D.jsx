// src/components/MarketPanel.jsx
{coins.map(coin => (
  <div key={coin} className="coin-tracker">
    <CandlestickChart data={marketData[coin]} />
    <div className="car-position">
      Position: {mapMarketToPosition(coin, activeIndicator, marketData[coin].value)}
    </div>
  </div>
))}
