def fib(n):
    if n == 1:
        return n

    elif n == 0:
        return 0

    else:
        return fib(n - 1) + fib(n - 2)

# Рекурсия 1: n = 7, else: return fib(6) + fib(5),    результат: 13
# Рекурсия 2: n = 6, else: return fib(5) + fib(4),    результат: 8
# Рекурсия 3: n = 5, else: return fib(4) + fib(3),    результат: 5
# Рекурсия 4: n = 4, else: return fib(3) + fib(2),    результат: 3
# Рекурсия 5: n = 3, else: return fib(2) + fib(1),    результат: 2
# Рекурсия 6: n = 2, else: return fib(1) + fib(0),    результат: 1
# Рекурсия 7: n = 1, if: return n,   результат: 1
