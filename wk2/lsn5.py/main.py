students = {
    'Andrei': {
        'int': 77,
        'str': 50,
        'if': 90
    },
    'Mirlan': {
        'int': 77,
        'str': 50,
        'if': 90
    },
    'Yasir': {
        'int': 77,
        'str': 50,
        'if': 90
    },
    'Aidar': {
        'int': 77,
        'str': 50,
        'if': 90
    },
    'Bekbolsun': {
        'int': 77,
        'str': 50,
        'if': 90
    },
}
# avg = {}
# for i in students:
#     avg.update(
#         {
#             i: sum(students[i].values()) / len(students[i].values())
#         }
#     )
# print(avg)
# print(other.get('second', 100))
# print(other.setdefault('fourth', 30))
# print(other)
#
# removed = other.popitem('first')
# print(other, removed)

# a = 0
# list1 = ['qw', 'er', 'ty', ]
# while True:
#     a += 1
#     b = input()
#     if a >= 3:
#         print('vy udalenny')
#         break
#     elif a < 3 and b in list1:
#         print('welcome')
#         break
#     elif a < 3 and b not in list1:
#         print('try again')
#         continue

from random import randint
print('goroda vse s malenkoi bukvy')
cities = ['bishkek', 'moskow', 'tashkent', 'karaganda', ]
random_city = cities[randint(0, 4)]
attempt = 2
new = '_'* len(random_city)
new_list = list(new)

while True:
    str1 = input('Enter letter: ')
    if attempt == 0:
        print('vy proigrali')
        break
    elif str1 not in random_city:
        attempt -= 1
        print('Takoi bukvy net, ostalos popytok:', attempt + 1)
        continue
    elif str1 in random_city:
        for i in range(len(random_city)):
            if str1 == random_city[i]:
                # print(type(new[i]), type(str1))
                new_list[i] = str1
                new = ''.join(new_list)
                continue
            elif str1 != random_city[i]:
                continue
        print(new)
    if random_city == new:
        print('vy pobedily')
        break


