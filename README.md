# Crypto Data Engineering Pipeline

Proyecto de ingeniería de datos que extrae información de criptomonedas desde la API de CoinGecko y la carga en PostgreSQL para su análisis mediante SQL.

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
- Git
- GitHub

## Estructura del proyecto

├── docs
├── scripts
│   └── etl_pipeline.py
├── sql
│   ├── market_summary.sql
│   └── top_10_cryptos.sql
├── README.md
└── requirements.txt

## Cómo ejecutar

Ejecutar el pipeline:

```bash
py scripts/etl_pipeline.py