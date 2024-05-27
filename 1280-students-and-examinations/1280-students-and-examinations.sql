# Write your MySQL query statement below
select st.student_id,
    st.student_name,
    su.subject_name,
    coalesce(count(ex.subject_name)) as attended_exams
from Students st
cross join subjects su
left join Examinations ex on ex.student_id = st.student_id and su.subject_name = ex.subject_name
group by ex.student_id,  st.student_name, su.subject_name
order by st.student_id, su.subject_name

-- coalesce(, 0) is used if count is null then 0 is used to show not attended students
-- cross join every detail of students with subject
-- left join for every detail of student and detail from examination on student_id and subject_name
-- group by student_id, student_name, subject_name
-- return in order of student_id and subject_name