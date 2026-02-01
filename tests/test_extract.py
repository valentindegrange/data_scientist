"""
Tests for the extract module
"""

import json
import tempfile
from pathlib import Path
from src.extract import extract_from_json, extract_from_csv, extract_data


def test_extract_from_json():
    """Test JSON extraction"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        test_data = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
        json.dump(test_data, f)
        temp_path = f.name
    
    try:
        result = extract_from_json(temp_path)
        assert len(result) == 2
        assert result[0]["name"] == "John"
    finally:
        Path(temp_path).unlink()


if __name__ == "__main__":
    test_extract_from_json()
    print("Tests passed!")
