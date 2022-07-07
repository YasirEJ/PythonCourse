#Condintions
# num1 = int(input('first number: '))
# op = input('operator: ')
# num2 = int(input('second number: '))
# if op == '+':
#     print(f'{num1} + {num2} = {num1 + num2}')
# elif op == '-':
#     print(f'{num1} - {num2} = {num1 - num2}')
# elif op == '/':
#     print(f'{num1} / {num2} = {num1 / num2}')
# elif op == '*':
#     print(f'{num1} * {num2} = {num1 * num2}')
# else:
#     print("i don't know operator which you wrote")
# or and
# list1 = [18, 30, 100, ]
# if 28 and 30 in list1:
#     print('hello')
# if 28 or 31 in list1:
#     print('hello')
# list1 = list(range(1000))
# list2 = []
# for i in list1:
#     if i % 15 == 0:
#         list2.append(i)
# print(list2)
# gradus = int(input())
# izmerenie = input().lower()
# if izmerenie == 'f':
#     print(f'{5/9 * (gradus - 32)} c = {gradus} f')
# elif izmerenie == 'c':
#     print(f'{9/5 * gradus + 32} f = {gradus} c')

# num1 = int(input())
# if num1 < -273.15:
#     print('ne mozhet byt')
# elif num1 == -273.15:
#     print('temperatura rovna nulya')
# elif num1 > -273.15 and num1 < 0:
#     print('temperatura menshe temperatu')
# elif num1 >  0 and num1 < 100:
#     print('obychnaya')
# elif num1 == 100:
#     print('temperatura na tochke kipenia')
# elif num1 > 100 :
#     print('temperatura vishe tochki kipenia')

# year = int(input())
# if year % 400 == 0 and year % 4 == 0 and year % 100 != 0:
#     print('YES')
# else:
#     print('NO')


num1 = int(input())
for i in range(1, 11):
    print(f'{num1} * {i} = {num1 * i}')