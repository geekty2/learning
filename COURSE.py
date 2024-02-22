import datetime

# Задайте дату
year = 2024
month = 2
day = 22

date = datetime.date(year, month, day)

# Отримайте день тижня
day_of_7 = date.weekday()  # Поверне 0 для понеділка, 1 для вівторка, ..., 6 для неділі
day_of_7_iso = date.isoweekday()  # Поверне 1 для понеділка, 2 для вівторка, ..., 7 для неділі

# Друк результату
print(day_of_7_iso)
