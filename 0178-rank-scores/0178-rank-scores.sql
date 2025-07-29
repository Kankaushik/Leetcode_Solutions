# Write your MySQL query statement below
SELECT 
  score,
  dense_RANK() OVER (ORDER BY score DESC) AS `rank`
FROM Scores;
