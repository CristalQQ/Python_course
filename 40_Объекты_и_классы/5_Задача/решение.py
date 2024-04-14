# 1. Создайте класс Image
# 2. У каждого экземпляра класса Image должно
# быть три собственных атрибута:
#   - resolution
#   - title
#   - extension
# 3. В классе должен быть метод resize, с помощью
# оторого можно поменять разрешение изображения.
# Вы должны просто менять значение атрибута resolution
# 4. Создайте несколько экземпляров класса Image и
# вызовите метод resize

class Image:
    def __init__(self, resolution, title, extention):
        self.resolution = resolution
        self.title = title
        self.extension = extention

    def resize(self, new_resolution):
        self.resolution = new_resolution

    def __str__(self):
        return self.title + '.' + self.extension


# Создаем экземпляр класса
one_image = Image('1200x900', 'Cat', 'png')
two_image = Image('1450x1000', 'dog', 'gif')
tree_image = Image('800x600', 'mouse', 'jpg')


# Проверяем результат
print(one_image.__dict__)
print(two_image.__dict__)
print(tree_image.__dict__)


# Изменяем атрибут resolutin с помощью метода класса resize
one_image.resize('1920x1800')
two_image.resize('1920x1800')
tree_image.resize('1920x1800')


print('')


# Проверяем результат
print(one_image.__dict__)
print(two_image.__dict__)
print(tree_image.__dict__)


print(one_image)
