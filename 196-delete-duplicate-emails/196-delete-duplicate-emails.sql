# Write your MySQL query statement below

#Reference two times the table to consider it as two separte copies
#And espicify from which alias you are deleting

DELETE p1
FROM Person AS p1, Person AS p2
WHERE p1.email = p2.email AND p1.id > p2.id
