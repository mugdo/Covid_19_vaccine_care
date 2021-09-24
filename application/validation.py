from .router import Reg
from datetime import  datetime, timedelta

def get_avalable_date(date):
    res = datetime.strptime(date, "%Y-%m-%d")
    res = (datetime.strptime(res.strftime('%Y-%m-%d'), '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')
    flag = True
    while flag:
        user_count = Reg.query.filter_by(date = res).count()
        print("user_count :", user_count)
        if user_count>2:
            print("enter")
            res = datetime.strptime(res, "%Y-%m-%d")
            res = (datetime.strptime(res.strftime('%Y-%m-%d'), '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')
            print("rest :", res)
            
        else: 
            flag = False
            break 
    datetime.strptime(res, "%Y-%m-%d")        
    return res
