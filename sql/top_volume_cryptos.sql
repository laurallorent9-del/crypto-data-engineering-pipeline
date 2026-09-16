SELECT
    name,
    symbol,
    total_volume
FROM crypto_prices
ORDER BY total_volume DESC
LIMIT 10;