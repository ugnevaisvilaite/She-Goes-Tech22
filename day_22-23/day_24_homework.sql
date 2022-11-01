# TODO 

* Task 1
* provide a query that shows total sales by each sales agent
* will require to join with the customer table
* will require to join with the invoice table


SELECT EmployeeId,
	e.FirstName || " " || e.LastName AS employees,
	sum(total) as Total_sales	
FROM employees e
JOIN invoices i  ON e.EmployeeId  = i.CustomerId 
JOIN customers c  ON e.EmployeeId = c.SupportRepId
group by EmployeeId


* Task 2
* QUERY TO find the top selling track of 2012
* will require use track table
* will requiret to join with invoice items table
* will require to join with the invoice table

SELECT 
	it.InvoiceId,
	count(*) AS Total_sales
FROM tracks t 
JOIN invoice_items it  ON t.TrackId  = it.TrackId 
JOIN invoices i  ON it.InvoiceId  = i.InvoiceId 
group by it.InvoiceId
ORDER BY Total_sales DESC 