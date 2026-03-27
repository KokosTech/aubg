def is_leap(year: int) -> bool:
    if (1900 <= year <= 2020) and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
        return True

    return False


def count_letter_case(string: str) -> tuple[int, int]:
    uppercase = 0
    lowercase = 0

    for letter in string:
        if (letter.isupper()):
            uppercase += 1

        if (letter.islower()):
            lowercase += 1

    return uppercase, lowercase

# only lambda and filter


def count_letter_case_special(string: str) -> tuple[int, int]:
    return len(list(filter(lambda x: x.isupper(), string))), \
        len(list(filter(lambda x: x.islower(), string)))


def print_nums(upper, lower=None, step=None):
    if upper and not any[lower, step]:
        x = range(upper + 1)
    elif step is None:
        if upper < lower:
            upper, lower = lower, upper

        x = range(lower, upper + 1)
    else:
        if upper < lower:
            upper, lower = lower, upper

        x = range(lower, upper + 1, step)

    for item in x:
        print(item)
