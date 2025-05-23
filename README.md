# recursion
Библиотека на Python, реализующая базовые алгоритмы с использованием рекурсии :

* Вычисление факториала числа
* Нахождение чисел Фибоначчи

## Структура проекта

`recursion/`  
├── `README.md` 
├── `__init__.py` 
├── `factorial/`  
│   ├── `__init__.py`  
│   └── `code.py`  
└── `fibonacci_sequence/`  
    ├── `__init__.py`  
    └── `code.py`  
    
## factorial
Содержит рекурсивную реализацию вычисления факториала числа .

> Факториал числа — это произведение всех целых чисел от 1 до этого числа.  
> Формула: n! = n * (n - 1) * (n - 2) * ... * 1

__Реализация через рекурсию:__
```bash
def factor(data):
    if data == 1:
        return 1
    else:
        return data * factor(data - 1)
```

__Пример работы:__
```bash
from factorial import factor

print(factor(5))                # Вывод: 120
```

__Как работает (шаги рекурсии):__
factor(5) → 5 * factor(4)  
factor(4) → 4 * factor(3)  
factor(3) → 3 * factor(2)  
factor(2) → 2 * factor(1)  
factor(1) → 1 (базовый случай)  
Итог: 5 * 4 * 3 * 2 * 1 = 120  


## fibonacci_sequence
Содержит рекурсивную реализацию нахождения чисел Фибоначчи.

> Число Фибоначчи — элемент последовательности, где каждый следующий элемент равен сумме двух предыдущих:
> F(n) = F(n-1) + F(n-2)
> При этом:
> F(0) = 0
> F(1) = 1

__Реализация через рекурсию:__
```bash
def fib(n):
    if n == 1:
        return n
    elif n == 0:
        return 0
    else:
        return fib(n - 1) + fib(n - 2)
```

__Пример работы:__
```bash
from fibonacci_sequence.code import fib

print(fib(7))  # Вывод: 13
```

__Как работает (шаги рекурсии):__
fib(7) → fib(6) + fib(5)  
fib(6) → fib(5) + fib(4)  
fib(5) → fib(4) + fib(3)  
fib(4) → fib(3) + fib(2)  
fib(3) → fib(2) + fib(1)  
fib(2) → fib(1) + fib(0)  
fib(1) → 1, fib(0) → 0  
Итог: fib(7) = 13  

## Установка
```bash
git clone https://github.com/dariadau/recursion
```
