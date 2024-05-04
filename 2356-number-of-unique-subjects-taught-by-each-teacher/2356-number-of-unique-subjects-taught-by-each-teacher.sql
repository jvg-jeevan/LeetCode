# Write your MySQL query statement below
-- take count() distinct subjects by grouping them according to teacher_id
select teacher_id, count(distinct subject_id) as cnt
from Teacher
group by teacher_id;