# pcost.py
#
# Exercise 1.27
def portfolio_cost(path):
    data=open(path,'r')
    headers=data.readline()
    tc=0
    for i in data:
        tc=(int(i.split(',')[1])*float(i.split(',')[2]))+tc
    return tc

tc=portfolio_cost('Data/portfolio.csv')
print(tc)