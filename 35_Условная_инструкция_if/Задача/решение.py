# 1. Создайте функцию route_info, которой будет передаваться словарь.
# 2. Если в словаре есть ключ distance и его значение целое число, верните строку
# "Dostance to your destinatiion is <distance>"
# 3. Иначе, если в словаре есть ключи speed и time, верните строку "Distance to your destination is <speed * time"
# 4. Иначе верните строку "No distance info is available"
# 5. Выховите функцию несколько раз с разными аргументами

def route_info(route):
    if ('distance' in route) and type(route['distance']) == int:
        return f"Dostance to your destinatiion is {route['distance']}"

    if ('speed' in route) and ('time' in route):
        return f"Distance to your destination is {route['speed'] * route['time']}"

    return "No distance info is available"


print(route_info({'distance': 15}))

print(route_info({'speed': 20, 'time': 3}))

print(route_info({'my_speed': 30}))
