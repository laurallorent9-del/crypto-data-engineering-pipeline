# Data Pipeline Architecture

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

## Data Flow

1. Extract cryptocurrency data from the CoinGecko API.
2. Transform and clean the dataset using Pandas.
3. Load processed data into PostgreSQL.
4. Run analytical SQL queries to generate insights.