# Data Engineering Master - Example Repository

This repository serves as an example for a Data Engineering Master's course, demonstrating basic data engineering concepts and practices.

## Project Structure

```
data_scientist/
├── src/                    # Source code modules
│   ├── extract.py         # Data extraction functions
│   ├── transform.py       # Data transformation functions
│   ├── load.py            # Data loading functions
│   └── etl_pipeline.py    # Complete ETL pipeline example
├── config/                 # Configuration files
│   └── config.yaml        # Project configuration
├── data/                   # Data directories
│   ├── raw/               # Raw input data
│   ├── processed/         # Processed/transformed data
│   └── output/            # Final output data
├── tests/                  # Unit tests
│   └── test_extract.py    # Example tests
├── notebooks/              # Jupyter notebooks for analysis
└── logs/                   # Log files
```

## Modules Overview

### Extract (`src/extract.py`)
Handles data extraction from various sources:
- JSON files
- CSV files
- Auto-detection of file types

### Transform (`src/transform.py`)
Provides data transformation and cleaning operations:
- String cleaning
- Type conversion
- Column name standardization
- Data filtering
- Aggregation functions

### Load (`src/load.py`)
Manages data loading to various destinations:
- JSON files
- CSV files
- Summary printing

### ETL Pipeline (`src/etl_pipeline.py`)
Demonstrates a complete ETL pipeline combining extract, transform, and load operations.

## Usage Examples

### Basic Extraction
```python
from src.extract import extract_data

data = extract_data('data/raw/input.json')
```

### Data Transformation
```python
from src.transform import standardize_column_names, clean_string

cleaned_data = standardize_column_names(data)
```

### Complete ETL Pipeline
```python
from src.etl_pipeline import run_etl_pipeline

run_etl_pipeline(
    source_path='data/raw/input.json',
    output_path='data/processed/output.json'
)
```

## Getting Started

1. Clone the repository
2. Explore the modules in the `src/` directory
3. Run the example scripts to understand the data flow
4. Modify and extend the code to fit your needs

## Learning Objectives

This repository demonstrates:
- Modular code organization
- ETL pipeline design
- Data extraction from multiple sources
- Data transformation and cleaning
- Data loading to various formats
- Best practices in data engineering
