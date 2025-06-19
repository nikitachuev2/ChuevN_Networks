import sqlite3
from datetime import datetime

import pandas as pd

from config import get_settings

DB = get_settings().db_path


def top_asns(limit: int = 10) -> pd.DataFrame:
    """Возвращает TOP-N автономных систем по числу запросов (HTTP+DNS)."""
    with sqlite3.connect(DB) as conn:
        df_http = pd.read_sql_query("SELECT asn, COUNT(*) AS hits FROM http_logs GROUP BY asn", conn)
        df_dns = pd.read_sql_query("SELECT asn, COUNT(*) AS hits FROM dns_logs  GROUP BY asn", conn)
    merged = (
        pd.concat([df_http, df_dns])
        .groupby("asn", as_index=False)
        .sum()
        .sort_values("hits", ascending=False)
        .head(limit)
    )
    return merged


def daily_growth(table: str = "http_logs") -> pd.DataFrame:
    """
    Считает прирост записей по дням.

    Parameters
    ----------
    table : {"http_logs", "dns_logs"}
    """
    with sqlite3.connect(DB) as conn:
        df = pd.read_sql_query(f"SELECT ts FROM {table}", conn, parse_dates=["ts"])
    df["date"] = df["ts"].dt.date
    return df.groupby("date").size().rename("records").to_frame()


if __name__ == "__main__":
    print("🏆 Топ-5 ASN:")
    print(top_asns(5))
    print("\n📈 Рост http_logs:")
    print(daily_growth("http_logs").tail())
