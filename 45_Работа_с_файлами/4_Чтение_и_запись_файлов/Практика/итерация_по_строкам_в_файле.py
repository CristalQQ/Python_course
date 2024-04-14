with open('text.txt', 'w') as test_file:
    test_file.write("First string\n")
    test_file.write("Second string\n")
    test_file.write("Third string\n")


with open('test.txt') as test_file:
    while True:
        line = test_file.readline()
        print(line)
        if not line:
            break
