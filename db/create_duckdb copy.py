import duckdb

con = duckdb.connect("db/unit-1-5.db")

con.sql("CREATE SCHEMA IF NOT EXISTS bypip")

con.sql(
    """
    CREATE TABLE bypip.address AS SELECT * FROM read_csv_auto('data/address.csv', HEADER=TRUE);
    CREATE TABLE bypip.car AS SELECT * FROM read_csv_auto('data/car.csv', HEADER=TRUE);
    CREATE TABLE bypip.claim AS SELECT * FROM read_csv_auto('data/claim.csv', HEADER=TRUE);
    CREATE TABLE bypip.client AS SELECT * FROM read_csv_auto('data/client.csv', HEADER=TRUE);
    """
)
