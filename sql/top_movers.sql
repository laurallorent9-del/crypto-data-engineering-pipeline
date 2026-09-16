SELECT
    name,
    symbol,
    price_change_percentage_24h
FROM crypto_prices
ORDER BY price_change_percentage_24h DESC
LIMIT 10;