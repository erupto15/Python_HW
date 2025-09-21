from Lesson_4.calculator import Calculator

calculator = Calculator()

print('start')
res = calculator.sum(4, 5)
assert res == 9
print('finish')