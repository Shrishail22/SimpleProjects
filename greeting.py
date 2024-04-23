import time
timestamp=time.strftime('%H:%M:%S')
print("Current Time is : ", timestamp)
timestamp=time.strftime('%H')
hours = int(timestamp)
if hours>=0 and hours<6:
    print("Good Morning")
elif hours >=6 and hours <12:
    print("Good Afternoon")
else:
    print("Good Evening")