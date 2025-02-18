import datetime
tdelta = datetime.timedelta(days=1)
yesterday = datetime.date.today() - tdelta
tomorrow = datetime.date.today() + tdelta
print(f" this is yesterday: {yesterday}, this is today: {datetime.date.today()}, this is tomorrow:  {tomorrow}")