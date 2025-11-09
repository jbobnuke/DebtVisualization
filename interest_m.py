class interest:
    def __init__(self, loan):
        self.loan = loan
        self.daily = loan.principle * (loan.interest / 100) / 365