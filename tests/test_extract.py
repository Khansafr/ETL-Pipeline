import pytest
from utils.extract import extract_data

def test_extract_data_structure():
    data = extract_data()
    assert isinstance(data, list)
    if data:  # test sample item
        sample = data[0]
        assert isinstance(sample, dict)
        assert "title" in sample
        assert "price" in sample
        assert "rating" in sample
        assert "colors" in sample
        assert "size" in sample
        assert "gender" in sample
        assert "timestamp" in sample
