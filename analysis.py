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


# %%
df.plot(kind="barh", x="First_Name", y="Total_Sales", legend=False)
plt.gca().invert_yaxis()
plt.xlabel("Total Spend ($)")
plt.title("Top 10 Customers by Spend")
plt.tight_layout()
plt.show()

# %%
query_genre = """
SELECT g.Name AS Genre_Name, ROUND(SUM(i.Quantity*i.UnitPrice),2) AS Total_Sales
FROM InvoiceLine AS i
JOIN Track AS t ON i.TrackId = t.TrackId
JOIN Genre AS g ON t.GenreId = g.GenreId
GROUP BY g.Name
ORDER BY Total_Sales DESC;
"""
df_genre = pd.read_sql_query(query_genre, conn)
df_genre

# %%
df_genre.plot(kind="barh", x="Genre_Name", y="Total_Sales", legend=False)
plt.gca().invert_yaxis()
plt.xlabel("Revenue ($)")
plt.title("Revenue by Genre")
plt.tight_layout()
plt.show()

# %%
query_monthly = """
SELECT SUM(Total) AS Total_Sales_Per_Month, strftime('%Y-%m',InvoiceDate) AS Month
FROM Invoice
GROUP BY strftime('%Y-%m',InvoiceDate)
ORDER BY Month ASC
"""
df_monthly = pd.read_sql_query(query_monthly, conn)
df_monthly["Rolling_3mo_Avg"] = df_monthly["Total_Sales_Per_Month"].rolling(3).mean()
df_monthly

# %%
plt.figure(figsize=(10,5))
plt.plot(df_monthly["Month"], df_monthly["Total_Sales_Per_Month"], label="Monthly Revenue", alpha=0.5)
plt.plot(df_monthly["Month"], df_monthly["Rolling_3mo_Avg"], label="3-Month Rolling Avg", linewidth=2)
plt.xticks(rotation=90)
plt.legend()
plt.title("Monthly Revenue with 3-Month Rolling Average")
plt.tight_layout()
plt.show()
# %%
