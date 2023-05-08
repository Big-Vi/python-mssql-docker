#!/bin/bash

# Start the script to create the DB and user
/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P $SA_PASSWORD -d master -i setup.sql & 

# Start SQL Server
/opt/mssql/bin/sqlservr