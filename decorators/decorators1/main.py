def deco(func):
    def wrapper(num):
        return func(num**2)
    return wrapper


@deco
def func(num):
    print(num)


print(func.__name__)
func(2)


def foo(num):
    print(num)


foo = deco(foo)
print(foo.__name__)
print(foo)
foo(2)
