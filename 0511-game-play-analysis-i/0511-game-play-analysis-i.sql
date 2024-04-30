# Write your MySQL query statement below
-- select the player id uniques, and the min login value of each player
select distinct player_id, min(event_date) as first_login
from Activity
group by player_id;