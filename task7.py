'''
*7. Числа Фибоначчи – это ряд чисел, в котором каждое следующее число равно
сумме двух предыдущих: 1, 1, 2, 3, 5, 8, 13, ...
Напишите программу, которая принимает на вход n номер в ряду, а отдает его значение.
'''
n = int(input("Введите номер в ряду: "))
sum = 0
count = 0

numberFib1 = 1
numberFib2 = 1

while count < n - 2:

    sum = numberFib2 + numberFib1
    numberFib1 = numberFib2
    numberFib2 = sum
    n += 1

print(numberFib2)

#Вывести ряд чисел Фибоначчи (через рекурсию)
# def Fib(n):
#         if n == 1 or n == 2:
#             return 1
#         else:
#             return Fib(n-2) + Fib(n-1)
# number = 30
# for i in range(1, number+1):
#     print(Fib(i))
