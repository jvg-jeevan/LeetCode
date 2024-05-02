SELECT 
    name,
    bonus
FROM Employee
LEFT JOIN Bonus USING (empID)
WHERE bonus < 1000 or bonus IS NULL;