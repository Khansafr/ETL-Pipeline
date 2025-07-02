from utils.extract import extract_data
from utils.transform import transform_data
from utils.load import save_to_csv

def main():
    print("Mulai proses ETL...")

    data = extract_data()
    print(f"Jumlah data mentah: {len(data)}")

    cleaned_df = transform_data(data)
    print(f"Jumlah data setelah transformasi: {len(cleaned_df)}")

    save_to_csv(cleaned_df)

if __name__ == "__main__":
    main()
