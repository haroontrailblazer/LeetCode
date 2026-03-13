
"""


177. Nth Highest Salary
Solved
Medium
Topics
SQL Schema
Pandas Schema
Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the nth highest distinct salary from the Employee table. If there are less than n distinct salaries, return null.

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
Example 2:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| null                   |
+------------------------+


"""





import pandas as pd

def nth_highest_salary(employees, N):
    df = pd.DataFrame(employees, columns = ['id','salary'])
    unique_values = df['salary'].drop_duplicates()
    sorted_values = unique_values.sort_values(ascending=False)
    
    if N <= len(sorted_values):
        return None
    
    else:
        return sorted_values.iloc[N-1]
    
    return pd.DataFrame({f'getNthHighestSalary({N})': [result]})

