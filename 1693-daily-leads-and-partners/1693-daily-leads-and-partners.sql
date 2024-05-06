# Write your MySQL query statement below
-- get the count of unique lead_id and partner_id
select 
    date_id, make_name, 
    count(distinct lead_id) as unique_leads,
    count(distinct partner_id) as unique_partners
from DailySales
group by date_id, make_name