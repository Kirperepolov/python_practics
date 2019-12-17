from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


def main():
    print(timedelta(days=365, hours=5, minutes=1))

    now = datetime.now()
    print('Today is:', str(now))
    print("One year from now it will be:", str(now + timedelta(days=365)))
    print("In 2 weeks 3 days and 20 hours from now it will be:", str(now + timedelta(weeks=2, days=3, hours=20)))

if __name__ == '__main__':
    main()
