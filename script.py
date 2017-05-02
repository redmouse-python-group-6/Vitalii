from datetime import date, time, datetime, timedelta
dt=date(year=2017,day=4,month=2)
now=date.today()
print(now)
print(dt)
tm=time(1, 12)
print(tm)
td=dt-now
print(type(td))
dati=datetime(2014, 12, 12, 12, 15)
dati_now=datetime.today()
dati_now=dati_now.replace(year=2018)
print(dati_now.replace(year=2018))
print(dati_now)
print(dati)
print(datetime.fromordinal(10000))
print(dati_now.replace(year=2018)-datetime.combine(dt, tm).replace(year=2018))
print(dati.timetuple())
print(datetime.now().isocalendar())
print(datetime.now().isoformat())
str_now=datetime.now().strftime("%d - %m - %y(%Y):%j T %% %I(%H):%M:%S %p")
print(str_now)
dt_now=datetime.strptime(str_now, "%d - %m - %y(%Y):%j T %% %I(%H):%M:%S %p")
print(dt_now)
print(dt_now.year)


import time
time.sleep(1)
print(time.asctime())

import calendar
c=calendar.TextCalendar()
print (c.monthdatescalendar(2017, 4))
c.prmonth(2017,4)
print(c.formatmonth(2017,4))
print(calendar.weekday(1990, 5, 2))