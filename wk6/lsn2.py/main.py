
# class ItSchool:
#     bootcamp_price = 15000
#     time = '8:30'

# student = ItSchool()
# student2 = ItSchool()
# student2.bootcamp_price = 15000
# student3 = ItSchool()

# print(student2.__dict__)

# class CarCarolla:
#     wheels = 4
#     volume = 1.8
#     engine = 'v6'
#     body = 'sedan'

#     def __init__(self, bumper, color, finishing) -> None:
#         self.bumper = bumper
#         self.color = color
#         self.finishing = finishing

#     def get_info(self):
#         print(f'{self.bumper}, car\'s color: {self.color}, car\'s finishing: {self.finishing}')

#     def change_otdelka(self, new):
#         self.finishing = new


# customer = CarCarolla('m obves', 'black', 'alcontaro')
# customer2 = CarCarolla('v obves', 'dark-blue', 'crocodile skin')
# print(customer.get_info())
# customer.change_otdelka('new_otdelka')
# print(customer.get_info())
# print(customer2.__dict__)


# lesson = {
#     'peremenii': 30,
#     'loops': 20
# }

# class Student:
#     group = 'bootcamp'
#     avg = 0

#     def __init__(self, fullname, age, lesson, ) -> None:
#         self.fullname = fullname
#         self.age = age
#         self.lesson = lesson

#     def get_info():
#         print(f"fullname: {self.fullname}, age: {self.age}, average ball: {avg}")
    
#     def set_avg(self):
#         for i in self.lesson.values():
#             avg += i
#         avg = avg / len(self.lesson)


# student = Student('Yasir', 13, lesson, )
# # student.set_avg()
# # student.get_info()
# print(type(student))


from random import randint


list = [[1, 2, 3, ],[4, 5, 6, ],[7, 8, 9, ]]

while True:
    players_choice = int(input(f'please, choose number of yacheika\n{list}\n'))
    while True:
        computer_choice = randint(0, 10)
        if computer_choice < 1 or computer_choice > 9:
            continue
        elif computer_choice >= 1 and computer_choice <= 9:
            break
    break