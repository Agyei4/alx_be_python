# PART1: Display the current Date and Time

# Importing libraries
import datetime
from datetime import datetime


def display_current_datetime():
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date}")
    return current_date

display_current_datetime()

def calculate_future_date():
    add_day = int(input("Enter the number of days to add to the current date: "))

    future_date = datetime.date.today() + datetime.timedelta(add_day)

    print(f"Future date: {future_date}")
    return future_date

calculate_future_date()