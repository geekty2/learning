from datetime import datetime, timedelta

# Отримуємо поточну дату
current_date = datetime.now()

# Визначаємо день тижня та дні до кінця тижня
days_until_end_of_week = 6 - current_date.weekday()

# Визначаємо дату кінця тижня
if days_until_end_of_week > 0:
    # Якщо кінець тижня ще не наступив
    end_date = current_date + timedelta(days=days_until_end_of_week)
else:
    # Якщо кінець тижня вже наступив, додаємо дні до наступного тижня
    days_until_next_week = 7 - current_date.weekday()
    end_date = current_date + timedelta(days=days_until_next_week)

print("Дата кінця тижня:", end_date.strftime("%d.%m.%Y"))
