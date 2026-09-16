CoinGecko API
        |
        v
+------------------+
|   ETL Pipeline   |
|     Python       |
+------------------+
        |
        v
+------------------+
|   PostgreSQL     |
|  crypto_prices   |
+------------------+
        |
        v
+------------------+
| SQL Analytics    |
| market_summary   |
| top_10_cryptos   |
+------------------+