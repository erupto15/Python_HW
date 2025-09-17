class Smartphone:
    def __init__(self, brand, model, phone_number):
        """Конструктор класса Smartphone"""
        self.brand = brand        # Бренд смартфона
        self.model = model        # Модель устройства
        self.phone_number = phone_number  # Номер телефона

    def get_info (self):
        return f"{self.brand} - {self.model}. {self.phone_number}"