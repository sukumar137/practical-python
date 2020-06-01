# mortgage.py
#
# Exercise 1.7
mortgage=500000
intrest=5/100
total_payment=2684.11
amount_paid=0
months=0
extra_payment_start_month=60
extra_payment_end_month=108
extra_payment=1000
while mortgage>0:
    months=months+1
    if months>=extra_payment_start_month and months<=extra_payment_end_month:
        mortgage=mortgage*(1+intrest/12)-(total_payment+extra_payment)
        amount_paid=amount_paid+total_payment+extra_payment
    else:
        mortgage=mortgage*(1+intrest/12)-total_payment
        amount_paid=amount_paid+total_payment
    print(months,'---',round(amount_paid,2),'------',round(mortgage,2))
