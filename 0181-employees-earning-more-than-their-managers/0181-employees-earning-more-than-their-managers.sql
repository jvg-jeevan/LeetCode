SELECT E.name AS 'Employee'
FROM Employee  E
INNER JOIN Employee P
ON P.id = E.managerID
Where E.salary > P.salary;