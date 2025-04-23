/*
=============================================================
Create Database and Schemas
=============================================================

My Datawarehouse is called TestDB because i already have a database called 'Datawarehouse' on my server

Script Purpose:
    This script creates a new database named 'TestDB' after checking if it already exists. 
    If the database exists, it is dropped and recreated. Additionally, the script sets up three schemas 
    within the database: 'bronze', 'silver', and 'gold'.
	
WARNING:
    Running this script will drop the entire 'TestDB' database if it exists. 
    All data in the database will be permanently deleted. Proceed with caution 
    and ensure you have proper backups before running this script.
*/

USE master;
GO

-- Drop and recreate the 'TestDb' database
IF EXISTS (SELECT 1 FROM sys.databases WHERE name = 'TestDb')
BEGIN
    ALTER DATABASE TestDb SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    DROP DATABASE TestDb;
END;
GO

-- Create the 'TestDb' database
CREATE DATABASE TestDb;
GO

USE TestDb;
GO

-- Create Schemas
CREATE SCHEMA bronze;
GO

CREATE SCHEMA silver;
GO

CREATE SCHEMA gold;
GO
