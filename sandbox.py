import loan_m
import interest_m
import dates_m
import numpy as np
import plotly.graph_objects as go




loan_1 = loan_m.loan(5000, 5.2, 60)

for i in range(11):
    
    days = dates_m.get_last_day_of_month(2025, i+1)
    loan_1.add_payment(50)
    loan_1.add_interest(days)
    print(loan_1.principle)

months, balance, total_paid = loan_1.evaluate_term(60)
x = list(range(1, months+2))
print(len(x))
print(len(balance))
fig = go.Figure(go.Scatter(x=x, y=balance, line_shape='spline'))
fig.show()