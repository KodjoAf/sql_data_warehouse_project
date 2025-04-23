import pandas as pd
import time
import os
from sqlalchemy import create_engine, text

# Database connection setup
def get_db_engine():
    """Establish and return a SQLAlchemy database engine.
        Put your own connection string here.
    """
    return create_engine(
        'mssql+pyodbc://SQOFFITD23W19E\DEVELOPPEMENT/TestDb?'
        'driver=ODBC+Driver+17+for+SQL+Server&'
        'Trusted_Connection=yes'
        )

# Function to truncate a table
def truncate_table(engine, table_name):
    """Truncate a given table."""
    print(f">> Truncating Table: {table_name}")
    with engine.connect() as conn:
        conn.execute(text(f"TRUNCATE TABLE {table_name}"))
        conn.commit()

# Function to bulk insert data using pandas
def bulk_insert(engine, table_name, file_path):
    """Bulk insert data from a CSV file into a specified table."""
    print(f">> Inserting Data Into: {table_name}")
    try:
        df = pd.read_csv(file_path)
        df.to_sql(table_name.split('.')[-1], engine, schema=table_name.split('.')[0], if_exists='replace', index=False)
        print(f">> Successfully loaded {len(df)} records into {table_name}")
    except Exception as e:
        print(f"Error loading {file_path}: {e}")

# Main function to load data into the Bronze schema
def load_bronze_layer():
    """Main function to load data into the Bronze schema."""
    start_time = time.time()
    print("================================================")
    print("Loading Bronze Layer")
    print("================================================")
    
    engine = get_db_engine()
    
    tables_files = {
        "bronze.crm_cust_info": "D:/Projects/sql-data-warehouse-project/datasets/source_crm/cust_info.csv", 
        "bronze.crm_prd_info": "D:/Projects/sql-data-warehouse-project/datasets/source_crm/prd_info.csv",
        "bronze.crm_sales_details": "D:/Projects/sql-data-warehouse-project/datasets/source_crm/sales_details.csv",
        "bronze.erp_loc_a101": "D:/Projects/sql-data-warehouse-project/datasets/source_erp/loc_a101.csv",
        "bronze.erp_cust_az12": "D:/Projects/sql-data-warehouse-project/datasets/source_erp/cust_az12.csv",
        "bronze.erp_px_cat_g1v2": "D:/Projects/sql-data-warehouse-project/datasets/source_erp/px_cat_g1v2.csv"
    }
    
    for table, file in tables_files.items():
        if os.path.exists(file):
            table_start_time = time.time()
            truncate_table(engine, table)
            bulk_insert(engine, table, file)
            print(f">> Load Duration: {round(time.time() - table_start_time, 2)} seconds")
            print("------------------------------------------------")
        else:
            print(f"File not found: {file}, skipping {table}")
    
    print("==========================================")
    print("Loading Bronze Layer is Completed")
    print(f"Total Load Duration: {round(time.time() - start_time, 2)} seconds")
    print("==========================================")

if __name__ == "__main__":
    load_bronze_layer()
