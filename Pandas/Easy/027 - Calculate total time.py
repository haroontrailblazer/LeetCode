import pandas as pd

def total_time(employees):
    df =  pd.DataFrame(employees)
    df['event_day'] = pd.to_datetime(df['event_day'])
    df['duration'] = df['out_time'] - df['in_time']
    
    res = (df.groupby(['event_day','day'],as_index=False)['duration'].sum().rename(columns={"event_day": "day", "duration": "total_time"}))
    return res


employees = {
    "emp_id": [1, 1, 1, 2, 2],
    "event_day": ["2020-11-28", "2020-11-28", "2020-12-03", "2020-11-28", "2020-12-09"],
    "in_time": [4, 55, 1, 3, 47],
    "out_time": [32, 200, 42, 33, 74]
}


total_time(employees)