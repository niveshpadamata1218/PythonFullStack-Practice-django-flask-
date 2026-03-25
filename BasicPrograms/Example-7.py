import datetime
import time
print(time.time())
print(time.asctime())
print(time.localtime())
time_time=time.asctime()
print(time_time)

from datetime import timedelta
x = datetime.datetime.now()
print("minus 90",x+timedelta(days=-90))
date_time = datetime.datetime.now()
print(date_time)
print("year:",date_time.year)
import calendar


s = calendar.month(2006,12)
print(s)
s1=calendar.isleap(2006)
print(s1)