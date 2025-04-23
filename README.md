# Data Warehouse and Analytic Project
This project showcases a comprehensive data warehousing and analytics solution, covering everything from building a data warehouse to deriving actionable insights. 
Designed as a portfolio project, it adheres to industry best practices in both data engineering and analytics.

# Data Architecture
The architecture used in this project is the medallion architecture (Bronze, Silver, Gold).

![high_level_architecture](https://github.com/user-attachments/assets/61f56c03-1ac7-402b-9cdb-ebe2b2383138)

1. **Bronze Layer**: Raw data is stored as-is from the source systems. It is ingested from CSV files into a SQL Server database.

2. **Silver Layer**: This layer involves data cleansing, standardization, and normalization processes to prepare the data for analysis. 

2. **Gold Layer**: Contains business-ready data modeled in a star schema, suitable for reporting and analytics.

# Project Overview
This project involves:

. **Data Architecture**: Designing a modern data warehouse using the Medallion Architecture with Bronze, Silver, and Gold layers.

. **ETL Pipelines**: Extracting, transforming, and loading data from source systems into the data warehouse.

. **Data Modeling**: Developing fact and dimension tables optimized for analytical queries.

. **Analytics & Reporting**: Creating SQL-based reports and dashboards to generate actionable insights.
