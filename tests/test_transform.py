import unittest
from utils.transform import transform_data

class TestTransform(unittest.TestCase):
    def setUp(self):
        self.raw_data = [{
            "title": "Test Shirt",
            "price": "10",
            "rating": "4.5 / 5",
            "colors": "3 Colors",
            "size": "Size: L",
            "gender": "Gender: Men",
            "timestamp": "2025-05-16"
        }]

    def test_price_conversion(self):
        df = transform_data(self.raw_data)
        self.assertEqual(df.iloc[0]["price"], 160000)

    def test_rating_conversion(self):
        df = transform_data(self.raw_data)
        self.assertEqual(df.iloc[0]["rating"], 4.5)

    def test_color_conversion(self):
        df = transform_data(self.raw_data)
        self.assertEqual(df.iloc[0]["colors"], 3)

    def test_dtypes(self):
        df = transform_data(self.raw_data)
        self.assertTrue(df["price"].dtype.kind in "fi")
        self.assertTrue(df["rating"].dtype.kind in "fi")
        self.assertTrue(df["colors"].dtype.kind in "i")

if __name__ == "__main__":
    unittest.main()
