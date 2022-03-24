# Write your MySQL query statement below

SELECT S1.score as score, COUNT(S2.score) AS "rank"
FROM Scores AS S1, 
(SELECT DISTINCT score from SCORES) AS S2
WHERE S1.score <= S2.score
GROUP BY S1.id
ORDER BY score DESC

