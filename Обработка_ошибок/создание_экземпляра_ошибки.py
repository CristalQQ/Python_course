def divide_nums(a, b):
    if b == 0:
        raise ValueError("Second argument can't be 0")
    return a / b

# Мы создаем экземпляр класса `ValueError`


try:
    divide_nums(10, 0)
except ValueError as e:
    print(e)  # Second argument can't be 0

print('Continue...')
