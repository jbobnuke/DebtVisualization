import interest_m
class loan:
    def __init__(self, principle, interest, term):
        self.principle = principle
        self.interest = interest
        self.term = term
    def monthly_payment(self):
        i = self.interest / 100 / 12
        P = self.principle
        n = self.term #months
        payment = P * (i * (1 + i)**n) / ((1 + i)**n - 1)
        return payment
    def add_payment(self, amount):
        if amount > self.principle:
            self.principle = 0
        else:
            self.principle -= amount
    def add_interest(self, days):
        daily_interest = interest_m.interest(self).daily
        self.principle += daily_interest * days
    def evaluate_term(self, monthly_payment):
        total_paid = 0
        months = 0
        balance = []
        balance.append(self.principle)
        while self.principle > 0:
            self.add_interest(30)
            self.add_payment(monthly_payment)
            total_paid += monthly_payment            
            months += 1
            balance.append(self.principle)
        return months, balance, total_paid