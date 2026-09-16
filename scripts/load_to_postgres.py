import pandas as pd
from sqlalchemy import create_engine

engine=create_engine(
    "postgresql://postgres:admin@localhost:5432/spotify_data"
)


df=pd.read_csv("data/crypto.csv")


df.to_sql(
    "crypto_prices",
    engine,
    if_exists="replace",
    index=False
)

print("Datos cargados en PostgreSQL correctamente")