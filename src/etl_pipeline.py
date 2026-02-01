"""
ETL Pipeline Module

This module demonstrates a complete ETL (Extract, Transform, Load) pipeline.
"""

from pathlib import Path
from typing import List, Dict, Any, Optional, Callable
from extract import extract_data
from transform import standardize_column_names, clean_string, apply_transformation
from load import load_to_file, print_summary


def run_etl_pipeline(
    source_path: str,
    output_path: str,
    transformations: Optional[List[Callable[[Dict[str, Any]], Dict[str, Any]]]] = None
) -> List[Dict[str, Any]]:
    """
    Run a complete ETL pipeline.
    
    Args:
        source_path: Path to the source data file
        output_path: Path to save the transformed data
        transformations: List of transformation functions to apply
        
    Returns:
        Transformed data
    """
    print("=" * 50)
    print("Starting ETL Pipeline")
    print("=" * 50)
    
    # Extract
    print(f"\n[EXTRACT] Reading data from: {source_path}")
    data = extract_data(source_path)
    print(f"Extracted {len(data)} records")
    
    # Transform
    print(f"\n[TRANSFORM] Applying transformations...")
    if transformations:
        for i, transform_func in enumerate(transformations, 1):
            print(f"  Applying transformation {i}...")
            data = apply_transformation(data, transform_func)
    
    # Standardize column names
    data = standardize_column_names(data)
    
    # Clean string values
    def clean_record(record: Dict[str, Any]) -> Dict[str, Any]:
        return {k: clean_string(v) if isinstance(v, str) else v 
                for k, v in record.items()}
    
    data = apply_transformation(data, clean_record)
    print(f"Transformed {len(data)} records")
    
    # Load
    print(f"\n[LOAD] Saving data to: {output_path}")
    load_to_file(data, output_path)
    print("Data saved successfully")
    
    # Summary
    print("\n[SUMMARY]")
    print_summary(data)
    
    print("\n" + "=" * 50)
    print("ETL Pipeline Completed")
    print("=" * 50)
    
    return data


if __name__ == "__main__":
    # Example usage
    print("ETL Pipeline Module")
    print("This module demonstrates a complete ETL pipeline.")
    print("\nTo run the pipeline, use:")
    print("  from src.etl_pipeline import run_etl_pipeline")
    print("  run_etl_pipeline('data/raw/input.json', 'data/processed/output.json')")
