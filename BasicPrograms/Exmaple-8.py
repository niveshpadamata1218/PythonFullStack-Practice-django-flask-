from datetime import datetime
import pytz
time1=pytz.timezone('Asia/Seoul')

print("Current time is",datetime.now(time1))