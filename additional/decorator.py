safe_function_call_mode = True


def safe_call(function):
    def wrapper():
        if not safe_function_call_mode:
            return function()
        try:
            return function()
        except Exception as exception:
            print(exception)
    return wrapper


@safe_call
def function():
    1 / 0


function()
input("Enter...")
