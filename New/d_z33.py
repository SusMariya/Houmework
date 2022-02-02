
### Чтобы вы подумали что не пыталась сделать домашнее задание, я пыталась, мой вариант написан первым, но
# понимаю что мой не правильный(((

class Person:
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age
    def __repr__(self):
        return f"{self.surname} {self.name} {self.age}"

class SortKey:
    def __init__(self, personlst):
        self.__personlst = personlst


    def __call__(self, *args, **kwargs):
        if len(args) == 1 and args[0] == 'surname':
            return sorted(self.__personlst, key=lambda Person: Person.surname)
        elif len(args) == 2 and args[0] == 'surname' and args[1] == "name":
            return sorted(self.__personlst, key=lambda Person:  Person.name)


p = [Person('Иванов', 'Игорь', 28),
     Person('Петров', 'Степан', 21),
     Person('Сидоров', 'Антон', 25),
     Person('Петров', 'Анатолий', 11),
     Person('Иванов', 'Иван', 28)]
g = SortKey(p)
print(g("surname"))

##########################################


class Person:
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    @property
    def data(self):
        return self.surname, self.name, self.age


class SortKey:
    def __init__(self, *args):
        self.__personlst = args

    def __call__(self, lst):
        lst.sort(key=lambda j: [j.__dict__[key] for key in self.__personlst])


p = [Person('Иванов', 'Игорь', 28),
     Person('Петров', 'Степан', 21),
     Person('Сидоров', 'Антон', 25),
     Person('Петров', 'Анатолий', 11),
     Person('Иванов', 'Иван', 28)]

for i in p:
    print(i.data)
print()

s1 = SortKey("surname")
s1(p)
for i in p:
    print(i.data)
print()
s2 = SortKey("surname", "name")
s2(p)
for i in p:
    print(i.data)
print()
