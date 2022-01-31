class Person:
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    @classmethod
    def sort(cls, surname):
        pass


class SortKey:
    def __init__(self, surname):
    # def __init__(self, surname, name, age):
    #     super().__init__(surname, name, age)
        self.__surname = surname

    def __call__(self, *args, **kwargs):
        return Person.sort(self.__surname)



p = [Person('Иванов', 'Игорь', 28),
     Person('Петров', 'Степан', 21),
     Person('Сидоров', 'Антон', 25),
     Person('Петров', 'Анатолий', 11),
     Person('Иванов', 'Иван', 28)]
g = SortKey(p)
for i in list(p):
    print(g())