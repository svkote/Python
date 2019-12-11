# Исключения (exceptions) - ещё один тип данных в python. Исключения необходимы для того, чтобы сообщать программисту
# об ошибках.
try:
    k = 1 / 0
except ArithmeticError:
    k = 0

print(k)
