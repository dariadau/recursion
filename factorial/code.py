def factor(data):
    if data == 1:  # базовый случай
        return 1

    else:  # рекурсивный  случай
        return factor(data - 1) * data


# Рекурсия 1: data = 5, else: func(4)    результат: 24 * 5 = 120
# Рекурсия 2: data = 4, else: func(3)    результат: 6 * 4 = 24
# Рекурсия 3: data = 3, else: func(2)    результат: 2 * 3 = 6
# Рекурсия 4: data = 2, else: func(1)    результат: 1 * 2 = 2
# Рекурсия 5: data = 1, if: return 1,        результат: 1
