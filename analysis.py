# %%
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("Chinook_Sqlite.sqlite")

# %%
query = """
SELECT c.CustomerId AS customer_id, c.FirstName AS First_Name, SUM(i.Total) AS Total_Sales
FROM Customer AS c
JOIN Invoice AS i ON c.CustomerId = i.CustomerId
GROUP BY c.CustomerId
ORDER BY Total_Sales DESC
LIMIT 10;
"""
df = pd.read_sql_query(query, conn)
df