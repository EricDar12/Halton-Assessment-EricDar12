# This file contains helper functions used throughout my data analysis
import os
import duckdb
import polars as pl
from dotenv import load_dotenv

load_dotenv()

# Reusable Variable Setup
def getConnection():
    dataset_path = os.getenv("LOCAL_DATASET_PATH")
    if not dataset_path:
        raise ValueError('Missing LOCAL_DATASET_PATH. Copy ".env.example" to ".env" and set the path.')
    # Create in-memory DuckDB connection
    con = duckdb.connect(database=":memory:")
    return con, dataset_path

