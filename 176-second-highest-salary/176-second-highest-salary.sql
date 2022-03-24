# Write your MySQL query statement below

#We nest two select to return null values when there is no secong higest salaray
SELECT (SELECT DISTINCT SALARY FROM Employee ORDER BY SALARY DESC LIMIT 1 OFFSET 1)  
AS SecondHighestSalary


