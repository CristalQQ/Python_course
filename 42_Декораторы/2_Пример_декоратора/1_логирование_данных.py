def log_function_call(fn):
    def wrapper(*args, **kwargs):
        print(f"Function name: {fn.__name__}")
        print(f"Function argument: {args}, {kwargs}")
        result = fn(*args, **kwargs)
        print(f"Function result: {result}")
        return result

    return wrapper


@log_function_call
def mult(a, b):
    return a * b


print(mult(5, 2))

print('')


@log_function_call
def sum(a, b):
    return a + b


print(sum(a=40.3, b=20.7))
