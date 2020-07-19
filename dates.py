import datetime as dt
import time as t
import dateparser

tnow = int(t.time())
print(tnow)
dtnow = dt.datetime.fromtimestamp(tnow)
print(dtnow)
print(dtnow.day, dtnow.month, dtnow.year)
print(dtnow.hour)
delta = dt.timedelta(days=100)
print(delta)
today = dt.date.today()
print(today+delta)
print(today>today+delta)
print(dt.datetime.fromtimestamp(1594642850+90*24*60*60))