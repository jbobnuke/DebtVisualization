import calendar
from datetime import date

def get_last_day_of_month(year, month):
    """
    Returns the last day of the specified month and year as a date object.
    """
    _, num_days = calendar.monthrange(year, month)
    return date(year, month, num_days).day

def days_between_dates(start, finish):
    """
    Returns the number of days between two date objects.
    """
    start_date = date(start[0], start[1], start[2])
    finish_date = date(finish[0], finish[1], finish[2])
    delta = finish_date - start_date
    return abs(delta.days)