# Эмулировать проверку авторизован ли пользователь, перед выполнением определенных действий в функции.
# Если пользователь не авторизован, то не будет выполняться функция, если авторизован - функция выполниться.

# Пользователь авторизировался - True
# Пользователь не авторизовался - False
def is_user_authenticated():
    return True  # True or False


def check_user_auth(fn):
    def wrapper(*args, **kwargs):
        if is_user_authenticated():
            print("User is authenticated!")
            return fn(*args, **kwargs)
        else:
            raise Exception("User is NOT authenticated")

    return wrapper


@check_user_auth
def do_sensitive_job():
    # Выполняйте некоторые задачи только в том случае, если пользователь прошел проверку подлинности.
    print("Results of some sensitive tasks")


try:
    do_sensitive_job()

except Exception as e:
    print(e)
