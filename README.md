# Crypto Data Engineering Pipeline

Personal Data Engineering project that extracts cryptocurrency data from the CoinGecko API, transforms it using Python and loads it into PostgreSQL for analytical SQL queries.

---

## Project Goal

The objective of this project is to build an end-to-end ETL pipeline following common Data Engineering practices:

- Extract data from a REST API
- Transform and clean the data
- Load the processed dataset into PostgreSQL
- Perform analytical queries using SQL
- Manage the project with Git and GitHub

---

## Architecture

```text
┌─────────────────┐
│ CoinGecko API   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Extract         │
│ Python Requests │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Transform       │
│ Pandas          │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Load            │
│ PostgreSQL      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ SQL Analytics   │
│ • Top 10        │
│ • Top Movers    │
│ • Top Volume    │
│ • Summary       │
└─────────────────┘
```

---

## Technologies

- Python
- Pandas
- Requests
- PostgreSQL
- SQLAlchemy
- SQL
- Git
- GitHub

---

## Project Structure

```text
crypto-data-engineering-pipeline

├── docs
│   └── architecture.md

├── scripts
│   └── etl_pipeline.py

├── sql
│   ├── market_summary.sql
│   ├── top_10_cryptos.sql
│   ├── top_movers.sql
│   └── top_volume_cryptos.sql

├── README.md

└── requirements.txt
```

---

## ETL Process

### Extract

Data is collected from the CoinGecko public API using Python and Requests.

### Transform

The dataset is cleaned and transformed using Pandas.

During development, a nested JSON field (`roi`) generated compatibility issues with PostgreSQL. This field was removed during the transformation stage before loading the data into the database.

### Load

The transformed dataset is loaded into PostgreSQL using SQLAlchemy.

---

## SQL Analytics

The project includes several analytical SQL queries:

### Top 10 cryptocurrencies by market capitalization

```sql
SELECT
    name,
    symbol,
    current_price,
    market_cap
FROM crypto_prices
ORDER BY market_cap DESC
LIMIT 10;
```

### Market summary

```sql
SELECT
    COUNT(*) AS total_cryptocurrencies,
    ROUND(AVG(current_price)::numeric, 2) AS average_price,
    SUM(market_cap) AS total_market_cap
FROM crypto_prices;
```

### Top cryptocurrencies by volume

```sql
SELECT
    name,
    symbol,
    total_volume
FROM crypto_prices
ORDER BY total_volume DESC
LIMIT 10;
```

### Top movers

```sql
SELECT
    name,
    symbol,
    price_change_percentage_24h
FROM crypto_prices
ORDER BY price_change_percentage_24h DESC
LIMIT 10;
```

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Pipeline

```bash
py scripts/etl_pipeline.py
```

---

## Key Learnings

Through this project I gained hands-on experience with:

- REST API consumption
- Data transformation with*Pandas
- ETL pipeline design
- PostgreSQL integration
- SQL analytics
- Git version control
- GitHub project management

---

## Author

Laura Llorent
