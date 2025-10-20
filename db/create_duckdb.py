import duckdb

con = duckdb.connect("db/unit-1-5.db")

# Create schema once
con.sql("CREATE SCHEMA IF NOT EXISTS bypip")

# Create each table explicitly
tables = ["address", "car", "claim", "client"]

for t in tables:
    con.sql(f"""
        CREATE OR REPLACE TABLE bypip.{t} AS
        SELECT * FROM read_csv_auto('data/{t}.csv', HEADER=TRUE);
    """)

# Verify results
con.sql("SET schema 'bypip';")
print(con.sql("SHOW TABLES;").fetchall())
