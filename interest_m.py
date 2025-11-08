class interest:
    def __init__(self, loan):
        self.loan = loan
        self.yearly = loan.interest
        self.monthly = loan.interest / 12
        self.daily = loan.interest / 365