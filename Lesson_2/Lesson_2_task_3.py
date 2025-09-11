import math


def square(side):
    area = side * side
    if not side.is_integer():
        return math.ceil(area)
    else:
        return area

test_cases = [5, 3.2, 7.8, 10, 4.5]
for side in test_cases:
    result = square(side)
    print(f"Сторона: {side}, Площадь: {result}")
