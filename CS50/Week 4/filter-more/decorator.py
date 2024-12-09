def dec(f):
    def wrapper(name):
        print("The start of the function...")
        f(name)
        print("The end of the function...")
    return wrapper


@dec
def hello(name):
    print(f"Hello {name}")


hello("Andrei")