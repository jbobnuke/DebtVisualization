import loan_m
import interest_m

loan_1 = loan_m.loan(5000, 5.2, 60)
interest_1 = interest_m.interest(loan_1)
print("monthly payment:", loan_1.monthly_payment())
print(interest_1.yearly)
print(interest_1.monthly)
print(interest_1.daily)