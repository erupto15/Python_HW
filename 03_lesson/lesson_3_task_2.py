from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 13", "+79123456789"))
catalog.append(Smartphone("Samsung", "Galaxy S22", "+79234567890"))
catalog.append(Smartphone("Xiaomi", "Mi 11", "+79345678901"))

print("Каталог смартфонов:")
for phone in catalog:
    print(phone.get_info())