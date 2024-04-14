import re

my_string = "My name is Vlad."
other_string = "My name is Vlad!"
all_string = "My name is Vlad. Vlad is instructor"

my_pattern = re.compile(r'^My.*\.$')
all_pattern = re.compile(r'V..d')

print(my_pattern)

print(my_pattern.search(my_string))


print(my_pattern.match(my_string))  # mathc() - ищет совпадение
print(my_pattern.match(other_string))
# Строка не соответствует регулярному выражению


print(all_pattern.findall(all_string))
# findall() - ищет все части строки, которые соответствуют патерну
