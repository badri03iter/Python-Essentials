from datetime import timedelta

def subtract_one_month(dt0):
    dt1 = dt0.replace(days=1)
    dt2 = dt1 - timedelta(days=1)
    dt3 = dt2.replace(days=1)
    return dt3

subtract_one_month