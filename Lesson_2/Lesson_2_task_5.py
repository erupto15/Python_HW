def month_to_season(month):
 if month == (12, 1, 2):
     return "Зима"
 if month == (3, 4, 5):
     return "Весна"
 if month == (6, 7, 8):
     return "Лето"
 if month == (9, 10, 11):
     return "Осень"
 else:
     return "Ошибка: введите число от 1 до 12"

test_months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for m in test_months:
 season = month_to_season(m)
 print(f"Месяц {m}: {season}")