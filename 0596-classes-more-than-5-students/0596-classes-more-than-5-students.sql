select class
from Courses
group by class
having count(class) > 4;
-- group the table based on class and get a count if >= 5 then select class