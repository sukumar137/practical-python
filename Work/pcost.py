# pcost.py
#
# Exercise 1.27
def portfolio_cost(path):
    try:
        data=open(path,'r')
        headers=data.readline()
        tc=0
        for i in data:
            tc=(int(i.split(',')[1])*float(i.split(',')[2]))+tc
        return tc
    except:
        file is not found

portfolio_cost('path')