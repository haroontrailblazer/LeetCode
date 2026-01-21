
"""
DataFrame animals
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| name        | object |
| species     | object |
| age         | int    |
| weight      | int    |
+-------------+--------+
Write a solution to list the names of animals that weigh strictly more than 100 kilograms.

Return the animals sorted by weight in descending order.

The result format is in the following example.

 

Example 1:

Input: 
DataFrame animals:
+----------+---------+-----+--------+
| name     | species | age | weight |
+----------+---------+-----+--------+
| Tatiana  | Snake   | 98  | 464    |
| Khaled   | Giraffe | 50  | 41     |
| Alex     | Leopard | 6   | 328    |
| Jonathan | Monkey  | 45  | 463    |
| Stefan   | Bear    | 100 | 50     |
| Tommy    | Panda   | 26  | 349    |
+----------+---------+-----+--------+
Output: 
+----------+
| name     |
+----------+
| Tatiana  |
| Jonathan |
| Tommy    |
| Alex     |
+----------+
Explanation: 
All animals weighing more than 100 should be included in the results table.
Tatiana's weight is 464, Jonathan's weight is 463, Tommy's weight is 349, and Alex's weight is 328.
The results should be sorted in descending order of weight.

"""



import pandas as pd

def findHeavyAnimals(animals):
    df = pd.DataFrame(animals, columns = ['name','species','age','weight'])
    dfc = df[df['weight'] > 100].sort_values(by = 'weight', ascending=False) [['name']]
    return dfc

animals = animals = [
    ["Tatiana",  "Snake",   98, 464],
    ["Khaled",   "Giraffe", 50, 41],
    ["Alex",     "Leopard", 6,  328],
    ["Jonathan", "Monkey",  45, 463],
    ["Stefan",   "Bear",    100, 50],
    ["Tommy",    "Panda",   26, 349]
]

findHeavyAnimals(animals)