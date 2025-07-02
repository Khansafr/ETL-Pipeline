import unittest
import os
import pandas as pd
from utils.load import save_to_csv

class TestLoad(unittest.TestCase):
    def test_save_to_csv(self):
        df = pd.DataFrame([{
            "title": "Test Shirt",
            "price": 160000,
            "rating": 4.5,
            "colors": 3,
            "size": "L",
            "gender": "Men",
            "timestamp": "2025-05-16"
        }])
        filename = "test_products.csv"
        
        # Simpan CSV
        save_to_csv(df, filename)
        
        # Cek file ada
        self.assertTrue(os.path.exists(filename))
        
        # Baca kembali file untuk verifikasi sederhana
        df_loaded = pd.read_csv(filename)
        self.assertEqual(df_loaded.iloc[0]["title"], "Test Shirt")
        self.assertAlmostEqual(df_loaded.iloc[0]["price"], 160000)
        
        # Hapus file setelah test selesai
        os.remove(filename)

if __name__ == "__main__":
    unittest.main()
