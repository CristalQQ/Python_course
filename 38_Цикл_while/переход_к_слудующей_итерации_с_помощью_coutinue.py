import random

random_num = random.randint(1, 5)
while True:
    num = int(input("Guess the number from 1 to 5: "))
    if num != random_num:   # Если не совпадает блок кода не выполняется
        print("Try again...")
        continue
    print("Congratulations!", random_num)
    break
