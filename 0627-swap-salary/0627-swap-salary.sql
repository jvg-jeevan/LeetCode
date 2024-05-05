-- using case similar to if else or switch in update
UPDATE Salary SET sex = 
CASE SEX 
    WHEN 'f' THEN 'm'
    WHEN 'm' THEN 'f'
END;