from datetime import datetime, timedelta


def transaction_start_end_time():
    return datetime.now().date().strftime("%d-%m-%Y"), (
        datetime.now().date() + timedelta(days=12)
    ).strftime("%d-%m-%Y")
