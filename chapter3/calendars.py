import calendar

c = calendar.TextCalendar(calendar.MONDAY)
print(c.formatmonth(2020, 1, 0, 0))
#     January 2020
# Mo Tu We Th Fr Sa Su
#        1  2  3  4  5
#  6  7  8  9 10 11 12
# 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26
# 27 28 29 30 31

hs = calendar.HTMLCalendar(calendar.MONDAY)
st = hs.formatmonth(2020, 1)
# print(st)
# <table border="0" cellpadding="0" cellspacing="0" class="month"> <tr><th colspan="7" class="month">January
# 2020</th></tr> <tr> <th class="mon">Mon</th><th class="tue">Tue</th> <th class="wed">Wed</th><th
# class="thu">Thu</th> <th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr> <tr><td
# class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="wed">1</td><td class="thu">2</td><td
# class="fri">3</td><td class="sat">4</td><td class="sun">5</td></tr> <tr><td class="mon">6</td><td
# class="tue">7</td><td class="wed">8</td><td class="thu">9</td><td class="fri">10</td><td class="sat">11</td><td
# class="sun">12</td></tr> <tr><td class="mon">13</td><td class="tue">14</td><td class="wed">15</td><td
# class="thu">16</td><td class="fri">17</td><td class="sat">18</td><td class="sun">19</td></tr> <tr><td
# class="mon">20</td><td class="tue">21</td><td class="wed">22</td><td class="thu">23</td><td class="fri">24</td><td
# class="sat">25</td><td class="sun">26</td></tr> <tr><td class="mon">27</td><td class="tue">28</td><td
# class="wed">29</td><td class="thu">30</td><td class="fri">31</td><td class="noday">&nbsp;</td><td
# class="noday">&nbsp;</td></tr> </table>

# loop over the days of month
# for d in c.itermonthdays(2020, 1):
    # print(d)

# loop over the month name (they depend on the local)
# for name in calendar.month_name:
#     print(name)

# Calculate days based on a rule
print("Team meetings will be on every first Friday of a month:")
for m in range(1, 13):
    cal = calendar.monthcalendar(2020, m)
    weekOne = cal[0]
    weekTwo = cal[1]

    if weekOne[calendar.FRIDAY] != 0:
        meetDay = weekOne[calendar.FRIDAY]
    else:
        meetDay = weekTwo[calendar.FRIDAY]

    # print("%10s %2d" % (calendar.month_name[m], meetDay))
