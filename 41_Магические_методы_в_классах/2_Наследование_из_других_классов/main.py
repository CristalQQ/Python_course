# Родительский класс, также известный как базовый класс или суперкласс, - это
# класс, от которого наследуются другие классы, называемые дочерними классами или
# подклассами. Родительский класс содержит общие атрибуты и методы, которые могут
# быть использованы его дочерними классами. Дочерние классы могут добавлять
# новые атрибуты и методы или изменять поведение унаследованных методов.


class ExtendedList(list):   # list - родительский класс, ExtendedList - дочерний
    # метод __init__ родительского класса вызывается автоматически
    def print_list_info(self):
        print(f"List has {len(self)} elements")


custom_list = ExtendedList([3, 5, 2])

custom_list.print_list_info()   # List has 3 elements

# Цепочка классов
# custom_list => ExtendedList => list => object

# Python ищет атрибуты сначала на уровне экземпляра класс (custom_list),
# если там нет, то на уровне дочернего класса ExtendedList,
# если там нет, то на уровне родительского класса list,
# если там нет, то на уровне базового класса object.

# Если Python нашел атрибут в первой цепочке, то на следующий уровень он не переходит.

# Пример 2:


class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass  # Абстрактный метод, который будет переопределен в дочерних классах


class Dog(Animal):
    def sound(self):
        return "Woof!"


class Cat(Animal):
    def sound(self):
        return "Meow!"


# Создаем экземпляры дочерних классов
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Вызываем метод sound для каждого экземпляра
print(dog.name, "says:", dog.sound())  # Выводит "Buddy says: Woof!"
print(cat.name, "says:", cat.sound())  # Выводит "Whiskers says: Meow!"
