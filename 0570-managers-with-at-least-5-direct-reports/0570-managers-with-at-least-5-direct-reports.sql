# Write your MySQL query statement below
select name
from Employee
where id in (
    select managerId
    from Employee
    group by managerId
    having count(*) > 4
);

-- sunquery returns the managerId where count is greater than or equal to 5
-- main query returns the names for the id's in subquery