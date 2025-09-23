
from string_utils import StringUtils

class TestCapitalizeMethod:
    def test_normal_string(self):
        # Тестируем обычный случай
        obj = StringUtils()
        result = obj.capitalize("skypro")
        assert result == "Skypro"

    def test_all_lowercase(self):
        # Тестируем строку, где все буквы строчные
        obj = StringUtils()
        result = obj.capitalize("skypro")
        assert result == "Skypro"

    # Негативные проверки

    def test_mixed_case(self):
        # Тестируем строку со смешанным регистром
        obj = StringUtils()
        result = obj.capitalize("SkYpRo")
        assert result == "Skypro"

    def test_leading_whitespace(self):
        # Тестируем строку с пробелом вначале
        obj = StringUtils()
        result = obj.capitalize("  Skypro")
        assert result == "Skypro"


# Второе тестирование

class TestTrimMethod:

    def test_no_whitespace(self):
        # Тестируем строку без пробелов
        obj = StringUtils()
        result = obj.trim("skypro")
        assert result == "skypro"


    def test_big_word(self):
        # Тестируем строку с большими буквами
        obj = StringUtils()
        result = obj.trim("SKYPRO")
        assert result == "Skypro"

# Негативные проверки

    def test_empty_string(self):
        # Тестируем пустую строку
        obj = StringUtils()
        result = obj.trim("")
        assert result == "", "Пустая строка должна остаться пустой"

    def test_normal_string(self):
        # Тестируем строку с пробелами в начале
        obj = StringUtils()
        result = obj.trim("   skypro")
        assert result == "skypro", "Должен быть удален пробел вначале"


class TestContainsMethod:
    def test_symbol_exists(self):
        # Тестируем наличие символа в строке
        obj = StringUtils()
        result = obj.contains("SkyPro", "S")
        assert result is True, "Символ должен быть найден"

    def test_symbol_not_exists(self):
        # Тестируем отсутствие символа в строке
        obj = StringUtils()
        result = obj.contains("SkyPro", "U")
        assert result is False, "Символа нет в строке"

    # Негативные проверки

    def test_empty_string(self):
        # Тестируем пустую строку
        obj = StringUtils()
        result = obj.contains("", "A")
        assert result is False, "В пустой строке не может быть символов"


class TestDeleteSymbolMethod:

    def test_single_symbol_deletion(self):
        # Тестируем удаление одного символа
        obj = StringUtils()
        result = obj.delete_symbol("SkyPro", "k")
        assert result == "SyPro", "Должен удалиться один символ"

    def test_substring_deletion(self):
        # Тестируем удаление подстроки
        obj = StringUtils()
        result = obj.delete_symbol("SkyPro", "Pro")
        assert result == "Sky", "Должна удалиться подстрока"

    # Негативные проверки

    def test_symbol_not_found(self):
        # Тестируем случай, когда символ не найден
        obj = StringUtils()
        result = obj.delete_symbol("SkyPro", "X")
        assert result == "SkyPro", "Строка должна остаться неизменной"

    def test_empty_string(self):
        # Тестируем пустую строку
        obj = StringUtils()
        result = obj.delete_symbol("", "A")
        assert result == "", "Пустая строка должна остаться пустой"