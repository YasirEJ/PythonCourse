

# profit = [10000, 15000, 20000, 11000, 9000, ]
# expenses = [1000, 100, 1134, ]

# def get_clear_income(profit: list, expenses: list):
#     return sum(profit) - sum(expenses)

# print(get_clear_income(profit, expenses))

# *args and **kwords


# from math import pow

# def get_arguments(*args: int, **kwargs):
#     result = []
#     # result2 = {}
#     # print(*args)
#     if args:
#         for i in args:
#             result.append(i**2)
#     if kwargs:
#         for key, values in kwargs.items():
#             if  type(values) == str:
#                 # result2[key] = values.upper()
#                 kwargs.update({
#                     key: values.upper()
#                 })
#             elif type(values) == set:
#                 # result2[key] = pow(values)    
#                 kwargs.update({
#                     key: [values]
#                 })
#     return result, kwargs

# print(get_arguments(1, 2, 3, 1, age=22, name='Yasir', sets = {1, 2}))

