# Write your MySQL query statement below
-- group the customers based on customer_nuumber and then order in desc and select the 1st customer_number
select customer_number 
from Orders
group by customer_number
order by count(customer_number) desc limit 1;