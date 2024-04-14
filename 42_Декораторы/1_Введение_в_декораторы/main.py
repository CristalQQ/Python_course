# Декораторы - это специальные функции, котороые автоматически выполняют ваши функции.

def decorator_functiion(original_fn):
    def wrapper_function():
        result = original_fn()

        return result

    return wrapper_function


@decorator_functiion    # Применение декоратора для функции
def my_function():
    print("This is my function!")


my_function()
