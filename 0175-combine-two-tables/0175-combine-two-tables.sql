SELECT 
    p.firstName,
    p.lastName,
    a.city,
    a.state
FROM Address a
RIGHT JOIN Person p on p.personId = a.personId;