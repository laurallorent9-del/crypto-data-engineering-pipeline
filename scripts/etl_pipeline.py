import requests
import pandas as pd
from sqlalchemy import create_engine


def extract():
    url = "https://api.coingecko.com/api/v3/coins/markets"

    params = {
        "vs_currency": "usd"
    }

    response = requests.get(url, params=params)

    return pd.DataFrame(response.json())


def transform(df):

    if "roi" in df.columns:
        df.drop("roi", axis=1, inplace=True)

    return df


def load(df):

    engine = create_engine(
        "postgresql://postgres:admin@localhost:5432/spotify_data"
    )

    df.to_sql(
        "crypto_prices",
        engine,
        if_exists="replace",
        index=False
    )


def main():

    df = extract()

    df = transform(df)

    load(df)

    print("Pipeline ejecutado correctamente")


if __name__ == "__main__":
    main()