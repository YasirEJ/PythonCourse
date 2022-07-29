# protected, private, public
a = input()

if a.isalnum():
    a = int(a)

class Ok:
    all_vowel = ['a', 'e', 'i', 'o', 'u']
    def __init__(self, message) -> None:
        self.message = message

    def return_message(self):
        if type(self.message) == str:
            list1 = []
            list2 = []
            for i in self.message:
                if i.lower() in self.all_vowel:
                    list1.append(i)
                elif i.isalnum():
                    pass
                else:
                    list2.append(i)
            if len(list2) * len(list1) <= len(self.message):
                return list1
            else:
                return list2
        elif type(self.message) in [int, float, complex, ]:
            a = 0
            b = 0
            for i in str(self.message):
                if i == '.' or i == '-':
                    b += 1
                    continue
                if int(i) % 2 == 0:
                    a += int(i)
            return a * (len(str(self.message)) - b)

customer = Ok(a)
print(customer.return_message())