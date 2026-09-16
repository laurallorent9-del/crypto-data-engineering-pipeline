# Crypto Data Engineering Pipeline

Proyecto personal de ingeniería de datos que extrae información de criptomonedas desde la API pública de CoinGecko, transforma los datos y los carga en PostgreSQL para su análisis mediante SQL.

## Objetivo

Construir un pipeline ETL completo utilizando herramientas habituales en ingeniería de datos.

## Arquitectura

CoinGecko API
    ↓
Extract
    ↓
Transform
    ↓
PostgreSQL
    ↓
SQL Analytics

## Tecnologías

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- SQL
- Git
- GitHub

## Estructura del proyecto

├── docs
│   └── architecture.md

├── scripts
│   └── etl_pipeline.py

├── sql
│   ├── top_10_cryptos.sql
│   └── market_summary.sql

├── README.md

└── requirements.txt

## Funcionalidades

- Extracción de datos desde una API REST.
- Limpieza y transformación de datos.
- Carga automática en PostgreSQL.
- Consultas analíticas mediante SQL.

## Consultas incluidas

### Top 10 criptomonedas por market cap

```sql
SELECT
    name,
    symbol,
    current_price,
    market_cap
FROM crypto_prices
ORDER BY market_cap DESC
LIMIT 10;