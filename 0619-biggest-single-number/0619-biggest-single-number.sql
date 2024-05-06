# Write your MySQL query statement below
select max(num) as num
from (select num 
from MyNumbers
group by num
having count(num)=1) as unique_values;
-- subquery return a table with single value (group the numbers and get the count)
-- main query get the maximum of numbers