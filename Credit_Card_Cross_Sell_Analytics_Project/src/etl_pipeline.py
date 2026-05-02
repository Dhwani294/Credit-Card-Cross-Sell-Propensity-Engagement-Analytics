
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import sqlite3
from pathlib import Path

RAW_PATH = "data/raw/BankChurners.csv"
OUTPUT_PATH = "data/processed/processed_credit_data.csv"

def load_data():
    df = pd.read_csv(RAW_PATH)
    return df

def clean_data(df):
    df.columns = df.columns.str.lower()

    df = df.loc[:, ~df.columns.str.contains("naive_bayes")]

    for col in df.select_dtypes(include=np.number).columns:
        df[col] = df[col].fillna(df[col].median())

    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].fillna(df[col].mode()[0])

    return df

def handle_outliers(df):
    numeric_cols = df.select_dtypes(include=np.number).columns

    for col in numeric_cols:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        df[col] = np.where(df[col] > upper, upper, df[col])
        df[col] = np.where(df[col] < lower, lower, df[col])

    return df

def feature_engineering(df):

    df['spend_velocity'] = (
        df['total_trans_amt'] / (df['months_on_book'] + 1)
    )

    df['engagement_score'] = (
        (df['total_trans_ct'] * 0.4) +
        (df['contacts_count_12_mon'] * -0.2) +
        (df['total_relationship_count'] * 0.4)
    )

    df['category_mix'] = (
        df['total_revolving_bal'] /
        (df['credit_limit'] + 1)
    )

    df['cross_sell_target'] = np.where(
        df['total_relationship_count'] > 4, 1, 0
    )

    return df

def save_outputs(df):

    Path("data/processed").mkdir(parents=True, exist_ok=True)

    df.to_csv(OUTPUT_PATH, index=False)

    conn = sqlite3.connect("data/processed/credit_analytics.db")
    df.to_sql("credit_customers", conn, if_exists="replace", index=False)
    conn.close()

def main():
    df = load_data()

    print(f"Initial Shape: {df.shape}")

    df = clean_data(df)
    df = handle_outliers(df)
    df = feature_engineering(df)

    print(f"Processed Shape: {df.shape}")
    print(f"Customers analyzed: {len(df)}")

    save_outputs(df)

    print("ETL pipeline completed successfully.")

if __name__ == "__main__":
    main()
