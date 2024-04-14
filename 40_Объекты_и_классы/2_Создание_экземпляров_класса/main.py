class Car:
    def move(self):
        print("Car is moving")

    def stop(self):
        print("Car is stopped")


my_car = Car()

print(my_car)   # my_car - является объектом и его местоположение в пямяти
print(type(my_car))  # этот объект является экземпляром класса Car
print(isinstance(my_car, Car))  # my_car является экземпляром класса Car
print(isinstance(my_car, object))   # my_car является экземпляром класса object


# Доступные атрибуты для объекта my_car
print(dir(my_car))


# Собственных атрибутов у объекта my_car нет, все атрибуты унаследованы от других классов (Car, object)
print(my_car.__dict__)


# Создадим еще один экземпляр класса Car
my_second_car = Car()

# Сравним два экземпляра
print(id(my_car) == id(my_second_car))  # False
# Это два независимых объекта
print(id(my_car), id(my_second_car))
# Объекты находяться в разных местах пямяти
