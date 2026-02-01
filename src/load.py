"""
Data Loading Module

This module handles loading data to various destinations.
"""

import json
import csv
from pathlib import Path
from typing import List, Dict, Any


def load_to_json(data: List[Dict[str, Any]], output_path: str) -> None:
    """
    Load data to a JSON file.
    
    Args:
        data: List of dictionaries to save
        output_path: Path to the output JSON file
    """
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_to_csv(data: List[Dict[str, Any]], output_path: str) -> None:
    """
    Load data to a CSV file.
    
    Args:
        data: List of dictionaries to save
        output_path: Path to the output CSV file
    """
    if not data:
        return
    
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    fieldnames = data[0].keys()
    
    with open(output_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def load_to_file(
    data: List[Dict[str, Any]], 
    output_path: str, 
    format_type: str = 'auto'
) -> None:
    """
    Load data to a file based on the file extension.
    
    Args:
        data: List of dictionaries to save
        output_path: Path to the output file
        format_type: Format type ('json', 'csv', or 'auto' for auto-detection)
    """
    path = Path(output_path)
    
    if format_type == 'auto':
        format_type = path.suffix.lower().replace('.', '')
    
    if format_type == 'json':
        load_to_json(data, output_path)
    elif format_type == 'csv':
        load_to_csv(data, output_path)
    else:
        raise ValueError(f"Unsupported format type: {format_type}")


def print_summary(data: List[Dict[str, Any]]) -> None:
    """
    Print a summary of the loaded data.
    
    Args:
        data: List of dictionaries with data
    """
    if not data:
        print("No data to summarize.")
        return
    
    print(f"Total records: {len(data)}")
    print(f"Fields: {', '.join(data[0].keys())}")
    
    if len(data) > 0:
        print("\nFirst record:")
        for key, value in list(data[0].items())[:5]:
            print(f"  {key}: {value}")


if __name__ == "__main__":
    # Example usage
    print("Data Loading Module")
    print("This module provides functions to load data to various destinations.")
