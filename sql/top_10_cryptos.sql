SELECT
    name,
    symbol,
    current_price,
    market_cap
FROM crypto_prices
ORDER BY market_cap DESC
LIMIT 10;