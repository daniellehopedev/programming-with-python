from datetime import datetime

user_name_input = input("Enter your name:\n")
user_name = user_name_input

user_input = input("Enter your goal with a deadline as a date separated by a colon:\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

# convert the string to a date format
deadline_date = datetime.strptime(deadline, "%m/%d/%Y")
# calculate the days from now to the deadline
today_date = datetime.today()
time_till = deadline_date - today_date

days_till = time_till.days
hours_till = int(time_till.total_seconds() / 60 / 60)
print(f"{user_name}! Time remaining for your goal: {goal} is {days_till} days and {hours_till} hours!")