SELECT
    COUNT(*) AS total_cryptocurrencies,
    ROUND(AVG(current_price)::numeric, 2) AS average_price
FROM crypto_prices;