# 1. Создайте функцию image_info с одним параметром типа img
# 2. Функция ожидает словарь, в котором должна быть как минимум два ключа:
# - image_id
# - image_title
# 3. Функция должна возвращать строку такого вида:
# "Image 'my cat' has id 5136"
# 4. Если хотя бы одного из этих ключей в словаре нет, функция должна
# генерировать ошибку TypeError
# 5. Вызовите функцию и корректно обработайте ошибку в случае возникновения

def image_info(img):
    if ('image_id' not in img) or ('image_title' not in img):
        raise TypeError("Keys image_id and image_title must be present")
    return f"Image '{img['image_title']}' has id {img['image_id']}"


try:
    print(image_info({'image_id': 5136, 'image_title': 'my cat'}))
    print(image_info({'error': 1, 'image_id': 5136}))
except TypeError as e:
    print(e)
