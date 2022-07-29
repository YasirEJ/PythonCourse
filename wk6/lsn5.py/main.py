# class Perent():

#     def work(self):
#         print('Worrking')

# class Child(Perent):

#     def play(self):
#         print('playing')

    
#     def work(self):
#         print('Working too long')

# child1 = Child()
# child1.play()
# child1.work()





# class Age:
#     def __init__(self, year):
#         self.year = year

#     def chinese_year(self):
#         return self.year * 3

#     def get_year(self):
#         from datetime import datetime
#         current_year = datetime.now().year
#         return current_year - self.year


# class NewAge(Age):
#     def __init__(self, year, rost):
#         super().__init__(year)
#         self.rost = rost

#     def get_rost(self, count_year):
#         if count_year + self.year < 25:        
#             result = self.rost + (4.7 * count_year)
#             current_year = self.year + count_year
#         elif count_year + self.year >= 25:        
#             result = (4.7 * 25 + self.rost)
#             current_year = self.year + count_year
#         print(f"В {current_year} году ваш рост будет {result} cm")

#     def new_get_year(self):
#         year_1 = super().get_year()
#         return year_1 + 1


# kunduz = NewAge(1996, 53)
# print(kunduz.get_year())
# print(kunduz.new_get_year())
# kunduz.get_rost(26)

# nazgul = NewAge()
#
# print(nazgul.get_year(1996))
# print(nazgul.new_get_year(1996))
# print(nazgul.chinese_year(1996))




### TASKS
# 2. Определить класс Car с полями название, цвет, цена, const полем CompanyName. 
# Создать  конструктор - дефолтный и с параметрами. Создать свойство доступа к полю цвет. 
# Определить методы Input () - для ввода данных о машине с консоли , 
# Print () - для вывода данных о машине на консоль и ChangePrice (float x) - для изменения цены на х% 
# Ввести данные о 3 авто. Уменьшить их цену на 10%, вывести данные об авто. 
# Ввести новый цвет и покрасить авто с цветом white в указанный цвет

# class Car:
#     company_name = 'Lexus'
#     def __init__(self, color, price, name) -> None:
#         self.color = color
#         self.price = price
#         self.name = name

#     @property
#     def color(self):
#         return self.color
    
#     @color.setter
#     def color(self, val):
#         self.color = val
#         return self.color

class Car:
    CompanyName = 'BEYMARAL'

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
    
    @property
    def get_color(self):
        return self.color

    @get_color.setter
    def get_color(self, val):
        self.color = val
        return self.color

    def print(self):
        return f'name: {self.name},\ncolor: {self.color},\nprice: {self.price},\nCompany name: {self.CompanyName}'
    
    def ChangePrice(self, x):
        self.price = self.price * x
        return self.price

    def input(self):
        self.color = input('Enter color ')
        self.name = input('Enter name of car ')
        self.price = int(input('Enter price '))

car = Car('black', 20, 'sedan')
print(car.color)
car.color = 'grey'
print(car.color)
car.input()

print(car.print())


