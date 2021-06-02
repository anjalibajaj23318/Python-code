from datetime import date, datetime
import pytz

utc=pytz.utc
list=pytz.timezone("Asia/Kolkata")

now=datetime.now(tz=utc)
list_now=now.astimezone(list)

print(now)
print(list_now)