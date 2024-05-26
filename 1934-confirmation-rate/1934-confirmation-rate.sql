-- sum(case) i.e like if confirmed 1 else 0 take sum of 1's and get the average for each user_id 
-- left join to include details of non confirmed details also

SELECT 
    u.user_id, 
    ROUND(SUM(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END) / COUNT(*), 2) AS confirmation_rate
FROM Signups u
LEFT JOIN Confirmations c ON u.user_id = c.user_id
GROUP BY u.user_id;