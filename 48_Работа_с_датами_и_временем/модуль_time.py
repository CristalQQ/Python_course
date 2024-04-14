import time

start_time = (time.time())


my_range = range(100000000)
print(my_range[1000])


end_time = (time.time())

print("Total duration if the operation ", end_time - start_time)
