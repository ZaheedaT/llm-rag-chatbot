#!/bin/bash

# This file will run when the Docker container starts.

# Run any setup steps or pre-processing tasks here
echo "Running ETL to move hospital data from csvs to Neo4j..."

# Run the ETL script
# An ETL script is a piece of code or program designed to perform the Extract, Transform, Load (ETL) process, which is essential in data integration and data pipeline workflows.
python hospital_bulk_csv_write.py

