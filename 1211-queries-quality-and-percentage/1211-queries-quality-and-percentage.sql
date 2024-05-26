# Write your MySQL query statement below

-- quality - average of division of rating and quality
-- sub query count of rating < 3 and average of that for each query_name and percentage of them grouping them with name of query_name

select query_name, 
    round(sum(rating/position)/count(query_name), 2) as quality,
    round((select count(*) from Queries q2 where q1.query_name = q2.query_name and q2.rating < 3) / count(*) * 100, 2) as poor_query_percentage 
from Queries q1
where query_name != 'null'
group by query_name;