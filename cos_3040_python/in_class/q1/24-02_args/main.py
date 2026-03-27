# Quiz Prep 2

# Exercise 2 -> Done
def generator_function(str_list):
    for s in sorted(str_list, key=len):
        yield s

# Exercise 3 -> Done


def var_args(*args, **kwargs):
    min_val = args[0]
    for arg in args:
        if arg < min_val:
            min_val = arg
    print(f'Minimum value: {min_val}')

    for key, value in kwargs.items():
        if value == min_val:
            print(f'{key} = {value}')

# Exercise 4 -> Done


def min_max(a: list[int]) -> tuple[int, int]:
    max = a[0]
    min = a[0]

    for i in a:
        if i > max:
            max = i
        if i < min:
            min = i

    return (max, min)


def odd_only(a: list[int]) -> list[int]:
    return [i for i in a if i % 2]


def sum(a: list[int]) -> int:
    total = 0
    for i in a:
        total += i
    return total

# Exercise 6 -> Done


def meta_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function name: {func.__name__}")

        print("Arguments passed: ")
        for a in args:
            print(a)

        print("Keyword arguments passed:")
        for key, value in kwargs.items():
            print(f"  {key}: {value}")

        print("Executing function...")

        res = func(*args, **kwargs)
        
        print("Function result: ", res)
        
        return res

    return wrapper

# Exercise 5 -> Done


@meta_decorator
def magic(a: list[int]):
    freq = dict()

    for i in a:
        freq[i] = freq.get(i, 0) + 1

    return freq


if __name__ == '__main__':
    print(magic([1, 2, 3, 4, 4, 6, 6, 8, 9]))
