from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


def main():
    print(timedelta(days=365, hours=5, minutes=1))  # 365 days, 5:01:00

    now = datetime.now()
    print('Today is:', str(now))
    # Today is: 2019-12-18 11:46:59.298880

    print("One year from now it will be:", str(now + timedelta(days=365)))
    # One year from now it will be: 2020-12-17 11:46:59.298880

    print("In 2 weeks 3 days and 20 hours from now it will be:", str(now + timedelta(weeks=2, days=3, hours=20)))
    # In 2 weeks 3 days and 20 hours from now it will be: 2020-01-05 07:46:59.298880

    # calculate some time before today
    t = now - timedelta(weeks=1, days=3, hours=11, minutes=32)
    s = t.strftime("%A, %B %d, %Y")
    print("some time ago was", s)

    # how many days until family reunion
    today = date.today()
    frd = date(today.year + 1, 1, 4)
    if frd < today:
        print("Girls already arrived %d days ago" % ((today - frd).days))
    else:
        print("Girls will be here in %d days" % ((frd - today).days))


if __name__ == '__main__':
    main()
