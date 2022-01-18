class Student:
    def __init__(self, name):
        self.name = name
        self.computer = self.Computer()

    def show(self):
        print(self.name, end="")
        self.computer.show()

    class Computer:
        def __init__(self):
            self.model = "HP"
            self.process = "i7"
            self.memory = 16
        def show(self):
            print(f" => {self.model}, {self.process}, {self.memory}")


outer = Student("Roman")
outer1 = Student("Vladimir")
outer.show()
outer1.show()


