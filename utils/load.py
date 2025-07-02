import pandas as pd

def save_to_csv(df, filename="products.csv"):
    try:
        df.to_csv(filename, index=False)
        print(f"Data berhasil disimpan sebagai CSV: {filename}")
    except Exception as e:
        print(f"Gagal menyimpan file CSV: {e}")
