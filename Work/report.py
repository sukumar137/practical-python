# report.py
#
# Exercise 2.4
def read_portfolio(path):
    import csv
    portfolio=[]
    with open(path,'r') as data:
        rows=csv.reader(data)
        headers=next(rows)
        for stock in rows:
            #s=stock.split(',')
            #print(stock)

            portfolio.append((stock[0],int(stock[1]),float(stock[2])))
    return portfolio

port=read_portfolio(r'Data\\portfolio.csv')
print(port)