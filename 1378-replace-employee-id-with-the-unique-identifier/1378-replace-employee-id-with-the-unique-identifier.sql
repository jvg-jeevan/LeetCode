SELECT 
    N.unique_id,
    E.name
FROM Employees E
LEFT JOIN EmployeeUNI N ON E.id = N.id;