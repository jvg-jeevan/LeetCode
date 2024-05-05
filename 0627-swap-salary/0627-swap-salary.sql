-- using case similar to if else in update
UPDATE Salary SET sex = 
CASE SEX 
    WHEN 'f' THEN 'm'
    ELSE 'f'
END;