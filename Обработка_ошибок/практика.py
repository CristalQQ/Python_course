try:
    print(10 / 0)
except ZeroDivisionError as e:
    print(type(e))
    print(e)

print('Continue...')
