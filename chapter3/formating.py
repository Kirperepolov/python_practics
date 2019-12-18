from datetime import datetime


def main():
    now = datetime.now()

    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    print(now.strftime("The current year is: %Y"))  # The current year is: 2019
    print(now.strftime("%a, %d %B, %y"))  # Tue, 17 December, 19

    # %c - locale's date and time, %x - locale's date, %X - locale's time
    print(now.strftime("\nLocale's date and time: %c"))     # Locale's date and time: Tue Dec 17 13:20:58 2019
    print(now.strftime("Locale's date: %x"))        # Locale's date: 12/17/19
    print(now.strftime("Locale's time: %X"))        # Locale's time: 13:20:58

    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print(now.strftime("\nCurrent time is: %I:%M:%S %p"))   # Current time is: 01:24:39 PM
    print(now.strftime("24-hour time: %H:%M:%S"))   # 24-hour time: 13:24:39

if __name__ == '__main__':
    main()
