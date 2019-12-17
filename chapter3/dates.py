# working with date information
from datetime import date
from datetime import time
from datetime import datetime

def main():
    today = date.today()
    print('Today is ', today)

    # print out the date's individual components
    print("Date components: ", today.day, today.month, today.year)

    # retrieve a weekday
    print('Today\'s weekday is:', today.weekday())
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print("Today is:", days[today.weekday()])

    # DAYTIME OBJECT
    today = datetime.now()
    print("\nThe current time is", today)

    # get the current time
    t = datetime.time(datetime.now())
    print(t)
    print(today.time())


if __name__ == '__main__':
    main()