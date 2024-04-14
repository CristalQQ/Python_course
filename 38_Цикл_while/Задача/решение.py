# 1. Создайте цикл, в котором нужно попросить пользователя
# ввести в терминале два числа.
# 2. Вывелите в терминал результат деления первого чила на второе
# 3. После этого спросите пользователя, хочет ли он продолжить yes/no
# 4. Если ответ no, то нужно выйти из цикла
# 5. Иначе нужно повторить все сначала


while True:
    try:
        num_one = float(input("Введите первое число: "))
        num_two = float(input("Введите первое число: "))
    except ValueError as e:
        print(e)
        print("You must enter numbers!")
        continue
    try:
        if num_two == 0:
            raise TypeError("На ноль делить нельзя")
    except TypeError as a:
        print(a)
        continue
    print(num_one / num_two)
    answer = input("Хотите продолжить? (yes/no): ")
    if answer == 'no':
        break
