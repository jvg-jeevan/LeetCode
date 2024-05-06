# Write your MySQL query statement below
select u.name as name, sum(t.amount) as balance
from Users u
join Transactions t on u.account = t.account
group by u.name
having sum(t.amount) > 10000;