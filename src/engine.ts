// src/engine/marketRacing.ts
export const mapMarketToPosition = (
  coin: string, 
  indicator: string, 
  value: number
): number => {
  // 1% market change = 5 track positions
  const sensitivity = {
    'HollowCandle': 1.2,
    'RSI': 0.8,
    'MACD': 1.0
  }[indicator] || 1.0
  
  return Math.floor(value * sensitivity * 5)
}
