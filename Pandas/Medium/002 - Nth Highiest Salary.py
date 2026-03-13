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

