
'''
Написати функцію, яка перебирає усі числа від a до b та виводить лише парні числа
'''

def print_even_numbers(a, b):
    # for i in range(a, b + 1):
    i = a
    while i <= b:
        if i % 2 == 0:
            print(i)
        i += 1
# Hello
# World
# 
print_even_numbers(1, 100)

# print(3 % 2)