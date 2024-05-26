# Write your MySQL query statement below
select *
from Users
where mail REGEXP '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode[.]com$';

-- ^[a-zA-Z] start with letter
-- prefix [a-zA-Z0-9_.-]* containg letters or char or num from this
-- [.] to match .
-- @leetcode[.]com$ ending of string '$' to check the domain 