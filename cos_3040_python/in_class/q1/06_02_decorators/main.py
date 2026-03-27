from functools import reduce


def multiplier(*args, **kwargs):
    res = 1
    for arg in args:
        res *= arg
    for key in kwargs:
        res *= kwargs[key]
    return res


print(multiplier(1, 2, 3, a=4, b=5))


def sum_decorator(func):
    def wrapper(num1, num2):
        num1 = abs(num1)
        num2 = abs(num2)
        return func(num1, num2)

    return wrapper


def general_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function name: {func.__name__}")

        print("Arguments: ")
        for arg in args:
            print(arg)

        print("Keyword Arguments: ")
        for key in kwargs:
            print(f"[{key}] -> {kwargs[key]}")

        print("Executing function...")

        return func(*args, **kwargs)

    return wrapper


@general_decorator
@sum_decorator
def sum_func(num1, num2):
    return num1 + num2


@general_decorator
def some_func(a, b, c):
    print(a, b, c)


print(sum_func(6, 7))
some_func(1, c=3, b=1)

result = list(map(lambda a, b: a * b, [1, 2, 3, 4], [0, 5, 10, 20]))
result = filter(lambda x: x > 0, [-1, 9, 8, 42])
result = reduce(lambda x, y: x + y, ["xx", "gdfg", "lol"])
