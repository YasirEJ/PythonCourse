#lambda

# som = lambda a, b: a + b
# print(som(2, 4))

# map


# leist = [1,2,3,4,5,6,7,8, ]

# list_square = list(map(lambda a: a**2, leist))
# list_mod = list(filter(lambda a: a if a % 2 == 0 else False, leist))
# print(list_mod)

# decorators

# def cook_burger(fucn):
#     def wrapper(m):
#         print('bulka')
#         print('tomato')
#         print('frie')
#         fucn(m)
#         print('salat')
#         print('bulka')
#     return wrapper

# @cook_burger
# def cotlet(meet):
#     print(meet)

# cotlet('beef')


def measure(func):
    def wrapper():
        from datetime import datetime
        start = datetime.now()
        func()
        end = datetime.now() - start
        return end
    return wrapper 

        
@measure
def func(URL):
    lists = [i for i in range(1, 100001)]
    return lists

# def list_for():
#     start = datetime.now()
#     lists = []
#     for i in range(1, 1000001):
#         lists.append(i)
#     print(lists)
print(list_comp())
