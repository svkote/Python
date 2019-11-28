def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


def print_one(arg1):
    print(f"arg1: {arg1}")


def print_none():
    print("Эта функция ничего не получает")


print_two("Михаил", "Райтман")
print_two_again("Михаил", "Райтман")
print_one("Первый")
print_none()
