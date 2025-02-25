import random
import datetime
from datetime import datetime,timedelta

def random_data(start , end):
    if isinstance(start,str):
        start=datetime.strptime(start , "%Y-%m-%d %H-%M-%S")
    if isinstance(end,str):
        end=datetime.strptime(end , "%Y-%m-%d %H-%M-%S")
    time_delta=end-start
    random_seconds=random.randint(0,int(time_delta.total_seconds()))
    return start+timedelta(seconds=random_seconds)
s="2024-01-01 00:00:00"
e="2025-01-01 23:59:59"
random_dt=random_data(s,e)
print(random_dt)