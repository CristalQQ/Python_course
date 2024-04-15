# Инструкция выполняет действие, например создает функцию `def` или
# запускает цикл `for`, `while`.
# С помощью инструкции можно вернуть результат функции `return`, или импортировать модуль `import`.

# Объявление класса и метода
class MyClass:
    def my_method(self):
        print("Hello from my method!")


# Обработка ошибок
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero!")
