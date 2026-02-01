"""
Data Extraction Module

This module handles data extraction from various sources.
"""

import json
import csv
from pathlib import Path
from typing import Dict, List, Any


def extract_from_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Extract data from a JSON file.
    
    Args:
        file_path: Path to the JSON file
        
    Returns:
        List of dictionaries containing the data
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data if isinstance(data, list) else [data]


def extract_from_csv(file_path: str) -> List[Dict[str, Any]]:
    """
    Extract data from a CSV file.
    
    Args:
        file_path: Path to the CSV file
        
    Returns:
        List of dictionaries containing the data
    """
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    return data


def extract_data(source_path: str, source_type: str = 'auto') -> List[Dict[str, Any]]:
    """
    Extract data from a file based on its type.
    
    Args:
        source_path: Path to the source file
        source_type: Type of source ('json', 'csv', or 'auto' for auto-detection)
        
    Returns:
        List of dictionaries containing the extracted data
    """
    path = Path(source_path)
    
    if source_type == 'auto':
        source_type = path.suffix.lower().replace('.', '')
    
    if source_type == 'json':
        return extract_from_json(source_path)
    elif source_type == 'csv':
        return extract_from_csv(source_path)
    else:
        raise ValueError(f"Unsupported source type: {source_type}")


if __name__ == "__main__":
    # Example usage
    print("Data Extraction Module")
    print("This module provides functions to extract data from various sources.")
