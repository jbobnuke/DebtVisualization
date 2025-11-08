import interest_m
class loan:
    def __init__(self, principle, interest, term):
        self.principle = principle
        self.interest = interest
        self.term = term
    def monthly_payment(self):
        i = interest_m.interest(self).monthly
        P = self.principle
        n = self.term #months
        payment = P * (i * (1 + i)**n) / ((1 + i)**n - 1)
        return payment