class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # Геттер для имени
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    # Геттер для фамилии
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    def full_name(self):
        print(f"Полное имя: {self.first_name} {self.last_name}")

# Пример использования:
user = User("Иван", "Иванов")
user.first_name()
user.last_name()      # Выведет: Фамилия: Иванов
user.full_name()                   # Выведет: Полное имя: Иван Иванов