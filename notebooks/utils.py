# This file contains helper functions used throughout my data analysis
import os
import duckdb
import polars as pl
from dotenv import load_dotenv

load_dotenv()

# Reusable Connection/Variable Setup
def getConnection():
    dataset_path = os.getenv("LOCAL_DATASET_PATH")
    if not dataset_path:
        raise ValueError('Missing LOCAL_DATASET_PATH. Copy ".env.example" to ".env" and set the path.')
    # Create in-memory DuckDB connection
    con = duckdb.connect(database=":memory:")
    return con, dataset_path

# Pass the connection and dataset path to easily build the temp table 
def readCSV(con, dataset_path):
    con.execute(f"""
    CREATE TEMP TABLE contracts AS
    SELECT *
    FROM read_csv_auto(
        '{dataset_path}',
        delim = ',',
        header = true,
        strict_mode = false,
        all_varchar = true
    )
    """)

# Encapsulated Data Cleaning Logic
def cleanContracts(con):
    con.execute("""
    CREATE OR REPLACE TABLE contracts_clean AS
    SELECT
        UPPER(TRIM(reference_number)) AS reference_number,
        
        commodity_code,

        NULLIF(TRIM(vendor_name), 'NA') AS vendor_name,
        NULLIF(TRIM(buyer_name), 'NA') AS buyer_name,
        
        procurement_id,
        
        TRY_CAST(contract_date AS DATE) AS contract_date,
        TRY_CAST(contract_period_start AS DATE) AS contract_period_start,
        TRY_CAST(delivery_date AS DATE) AS delivery_date,
        
        TRY_CAST(REPLACE(contract_value, ',', '') AS DOUBLE) AS contract_value,
        TRY_CAST(REPLACE(original_value, ',', '') AS DOUBLE) AS original_value,
        TRY_CAST(REPLACE(amendment_value, ',', '') AS DOUBLE) AS amendment_value,
        
        CASE WHEN UPPER(TRIM(former_public_servant)) = 'Y' THEN TRUE ELSE FALSE END AS former_public_servant,
        
        TRIM(owner_org) AS owner_org,
        TRIM(owner_org_title) AS owner_org_title,
        
        ROW_NUMBER() OVER (
            PARTITION BY reference_number
            ORDER BY TRY_CAST(contract_date AS DATE) DESC
        ) AS rn
    FROM contracts
    WHERE reference_number IS NOT NULL
    """)

