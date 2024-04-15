# Переписать пример используя инструкцию if else

# my_img = ('1920', '1080')

# print(f"{my_img[0]}x{my_img[1]}") if len(
#     my_img) == 2 else print("Incorrect image formatting")

my_img = ('1920', '1080')

if len(my_img) == 2:
    print(f"{my_img[0]}x{my_img[1]}")
else:
    print("Incorrect image formatting")
