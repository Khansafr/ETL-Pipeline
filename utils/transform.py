import pandas as pd

def transform_data(data):
    try:
        df = pd.DataFrame(data)

        # Drop baris dengan title, price, atau rating yang invalid
        invalid_titles = ["Unknown Product", None]
        invalid_prices = ["Price Unavailable", None]
        invalid_ratings = ["Invalid Rating / 5", "Not Rated", None]

        df = df[~df["title"].isin(invalid_titles)]
        df = df[~df["price"].isin(invalid_prices)]
        df = df[~df["rating"].isin(invalid_ratings)]

        # Konversi price ke float dan ubah ke IDR (kurs 1 USD = 16,000 IDR)
        df["price"] = pd.to_numeric(df["price"], errors="coerce") * 16000

        # Ekstrak angka dari rating (misal: "4.5 / 5" -> 4.5)
        df["rating"] = df["rating"].astype(str).str.extract(r"([\d.]+)")[0]
        df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

        # Ekstrak angka dari colors, default ke 1 jika kosong
        df["colors"] = df["colors"].astype(str).str.extract(r"(\d+)")[0].fillna("1")
        df["colors"] = pd.to_numeric(df["colors"], errors="coerce")

        # Bersihkan label Size dan Gender (hapus prefix dan spasi)
        df["size"] = df["size"].astype(str).str.replace("Size:", "", regex=False).str.strip()
        df["gender"] = df["gender"].astype(str).str.replace("Gender:", "", regex=False).str.strip()

        # Drop baris yang mengandung null di kolom utama
        required_columns = ["price", "rating", "colors", "size", "gender"]
        df.dropna(subset=required_columns, inplace=True)

        # Drop duplikat seluruh baris
        df.drop_duplicates(inplace=True)

        # Reset index
        df.reset_index(drop=True, inplace=True)

        # Jika kolom timestamp tidak ada, tambahkan dengan NaT
        if "timestamp" not in df.columns:
            df["timestamp"] = pd.NaT
        else:
            # Konversi kolom timestamp ke tipe datetime
            df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

        # Tetapkan tipe data kolom
        df = df.astype({
            "title": "object",
            "price": "float64",
            "rating": "float64",
            "colors": "int64",
            "size": "object",
            "gender": "object",
            # timestamp sudah datetime64[ns] setelah konversi
        })

        return df

    except Exception as e:
        print(f"[Transform Error] {e}")
        return pd.DataFrame()
