import datetime, bday_messages as bd

today = datetime.date.today()
next_birthday = datetime.date(2026, 8, 23)

days_away = (next_birthday - today).days

if days_away == 0:
    print(bd.random_message)
else:
    print(f'My next birthday is {days_away} days away!')