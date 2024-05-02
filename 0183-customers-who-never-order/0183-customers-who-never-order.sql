SELECT c.name as customers
FROM Customers c 
LEFT JOIN Orders o ON c.id = o.customerID
where o.customerID IS NULL;