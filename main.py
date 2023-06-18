# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

number = input('Введите  трехзначное число a=')
number = int(number)
sum = 0

if number >= 100 and number <= 999:
    while number > 0:
        sum += number % 10 
        number//=10
    print(f'сумма цифр введденного числа ={sum}')
else:
    print('Введино не трехзначное число')