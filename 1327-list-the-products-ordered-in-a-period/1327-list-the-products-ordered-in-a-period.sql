select p.product_name, sum(o.unit) as unit
from Products p
join Orders o on p.product_id = o.product_id
-- to select values between dates
where o.order_date between '2020-02-01' and '2020-02-29'
-- group based on product id
group by o.product_id
-- select units >= 100
having sum(o.unit) >= 100;