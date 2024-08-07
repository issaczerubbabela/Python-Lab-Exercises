import datetime

def days_until_future_date(future_date):
    today = datetime.date.today()
    remaining_days = (future_date - today).days
    return remaining_days

desired_date_str = input("Enter a future date (YYYY-MM-DD): ")
desired_date = datetime.datetime.strptime(desired_date_str, "%Y-%m-%d").date()  # Replace with your desired future date
remaining_days = days_until_future_date(desired_date)
print(f"There are {remaining_days} days remaining until {desired_date}.")

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Example usage:
year_to_check = int(input('enter the year to check: '))  # Replace with the year you want to check
if is_leap_year(year_to_check):
    print(f"{year_to_check} is a leap year.")
else:
    print(f"{year_to_check} is not a leap year.")
