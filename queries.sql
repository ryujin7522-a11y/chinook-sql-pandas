--Top 10 customers by total spend
SELECT RANK() OVER (
        ORDER BY SUM(i.Total) DESC
    ) AS Ranking,
    c.FirstName AS First_Name,
    SUM(i.Total) AS Total_Sales
FROM Customer AS c
    JOIN Invoice AS i ON c.CustomerId = i.CustomerId
GROUP BY c.CustomerId
ORDER BY total_sales DESC --Which genres bring in the most revenue
SELECT g.Name AS Genre_Name,
    ROUND(SUM(i.Quantity * i.UnitPrice), 2) AS Total_Sales
FROM InvoiceLine AS i
    JOIN Track AS t ON i.TrackId = t.TrackId
    JOIN Genre AS g ON t.GenreId = g.GenreId
GROUP BY g.Name
ORDER BY Total_Sales DESC;
--Monthly revenue trend
SELECT SUM(Total) AS Total_Sales_Per_Month,
    strftime('%Y-%m', InvoiceDate) AS Month
FROM Invoice
GROUP BY strftime('%Y-%m', InvoiceDate)
ORDER BY Month ASC --Which countries generate the most revenue 
SELECT SUM(Total) AS Total_Sales,
    BillingCountry AS Country
FROM Invoice
GROUP BY BillingCountry
ORDER BY Total_Sales DESC --Which customers have purchased at least one track from every single media type?
SELECT c.CustomerId AS Customer_Id,
    c.FirstName AS Customer_Name
FROM Track AS t
    JOIN InvoiceLine AS i ON i.TrackId = t.TrackId
    JOIN Invoice AS ie ON ie.InvoiceId = i.InvoiceId
    JOIN Customer AS c ON c.CustomerId = ie.CustomerId
GROUP BY c.CustomerId
HAVING COUNT(Distinct t.MediaTypeId) = (
        SELECT COUNT(*)
        FROM MediaType
    )