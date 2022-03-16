# Write your MySQL query statement below

#Create two intances of the Employee table, one for the employee and one for the manager.

SELECT employee.name as Employee FROM Employee as employee, Employee as manager
WHERE employee.salary > manager.salary and employee.managerID = manager.id

