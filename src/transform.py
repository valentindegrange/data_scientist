"""
Data Transformation Module

This module handles data transformation and cleaning operations.
"""

from typing import List, Dict, Any, Callable, Optional


def clean_string(value: Any) -> Optional[str]:
    """
    Clean string values by removing whitespace and handling None values.
    
    Args:
        value: Value to clean
        
    Returns:
        Cleaned string or None
    """
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip() if value.strip() else None
    return str(value).strip() if str(value).strip() else None


def convert_to_numeric(value: Any, default: float = 0.0) -> float:
    """
    Convert a value to numeric type.
    
    Args:
        value: Value to convert
        default: Default value if conversion fails
        
    Returns:
        Numeric value
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        return default


def standardize_column_names(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Standardize column names to lowercase with underscores.
    
    Args:
        data: List of dictionaries with data
        
    Returns:
        List of dictionaries with standardized column names
    """
    standardized = []
    for record in data:
        new_record = {}
        for key, value in record.items():
            new_key = key.lower().replace(' ', '_').replace('-', '_')
            new_record[new_key] = value
        standardized.append(new_record)
    return standardized


def apply_transformation(
    data: List[Dict[str, Any]], 
    transformation: Callable[[Dict[str, Any]], Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """
    Apply a transformation function to each record in the data.
    
    Args:
        data: List of dictionaries with data
        transformation: Function to apply to each record
        
    Returns:
        Transformed data
    """
    return [transformation(record) for record in data]


def filter_data(
    data: List[Dict[str, Any]], 
    condition: Callable[[Dict[str, Any]], bool]
) -> List[Dict[str, Any]]:
    """
    Filter data based on a condition.
    
    Args:
        data: List of dictionaries with data
        condition: Function that returns True for records to keep
        
    Returns:
        Filtered data
    """
    return [record for record in data if condition(record)]


def aggregate_data(
    data: List[Dict[str, Any]], 
    group_by: str, 
    agg_func: Callable[[List[Any]], Any]
) -> Dict[str, Any]:
    """
    Aggregate data by a specific field.
    
    Args:
        data: List of dictionaries with data
        group_by: Field name to group by
        agg_func: Aggregation function to apply
        
    Returns:
        Dictionary with aggregated results
    """
    groups = {}
    for record in data:
        key = record.get(group_by)
        if key not in groups:
            groups[key] = []
        groups[key].append(record)
    
    return {key: agg_func(values) for key, values in groups.items()}


if __name__ == "__main__":
    # Example usage
    print("Data Transformation Module")
    print("This module provides functions to transform and clean data.")
