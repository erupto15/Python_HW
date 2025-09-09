def month_to_season(month):
 if month == 12:
     return "Зима"
 else:
     return "Ошибка: введите число от 1 до 12"

test_months = [12]

for m in test_months:
 season = month_to_season(m)
 print(f"Месяц {m}: {season}")