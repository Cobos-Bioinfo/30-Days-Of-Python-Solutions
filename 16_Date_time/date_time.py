# Day 14 - 30DaysOfPython Challenge
# Higher order functions
from datetime import datetime


# 1 - Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.now()
# ":02d" Adds 0-padding (0=pad with 0, 2=width of 2, d=decimal integer (no decimal points))
print(
    f"Current Date (dd/mm/yyyy): {now.day:02d}/{now.month:02d}/{now.year}\n"
    f"Current Time (hh:min): {now.hour:02d}:{now.minute:02d}\n"
    f"Timestamp: {now.timestamp()}"
)

# 2 - Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
print(
    f"Current Date: {now.strftime("%b. %d, %Y")}\n"
    f"Current Time: {now.strftime("%H:%M:%S")}"
)

# 3 - Today is 5 December, 2019. Change this time string to time.
print(datetime.strptime("5 December, 2019", "%d %B, %Y"))

# 4 - Calculate the time difference between now and new year.


# 5 - Calculate the time difference between 1 January 1970 and now.


# 6 - Think, what can you use the datetime module for? Examples:
    
    
    # Time series analysis
    
    
    # To get a timestamp of any activities in an application
    
    
    # Adding posts on a blog