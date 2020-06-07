# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
total_paid = 0.0

extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000
month = 1

while principal > 0:
    payment = 2684.11
    if month <= extra_payment_end_month and month >= extra_payment_start_month: 
        payment = payment + extra_payment
    not_very_much_payment = principal * (1+rate/12) - payment >= 0 
    if not_very_much_payment:    
        principal = principal * (1+rate/12) - payment
    else: 
        payment = principal * (1+rate/12) 
        principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    if principal > 0:
        month += 1
    print(f'{month} {total_paid:0.2f} {principal:0.2f}')

print(f'Total paid {total_paid:0.2f}')
print(f'Months {month}')


