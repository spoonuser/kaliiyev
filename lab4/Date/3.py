import datetime
date_now = datetime.datetime.now()
date_without_microsec = date_now.replace(microsecond = 0)
print(date_without_microsec)