PROVIDER = "sql_server"

CONNSTR = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    + "SERVER=localhost;"
    + "DATABASE=AdventureWorks;"
    + "Trusted_Connection=yes;"
)

QUERY = """
    SELECT DISTINCT TOP 5 FirstName, LastName
    FROM Person.Person
    ORDER BY LastName, FirstName;
"""
