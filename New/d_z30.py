import re
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self._model=self.Computer.model
#
#         print(f"{self.name}=> {self.Computer.model}, {self.Computer._process}, {self._memory}")
#             print(self.name, => self.Computer.model, self.Computer._process, self._memory)
#
#     class Computer:
#         def __init__(self, model, process, memory):
#             self._model = model
#             self._process = process
#             self._memory=memory

class Student:
    def __init__(self, name):
        self.name = name
        # self.computer = self.Computer()
        # print(f"{self.name}=> {self.Computer.model}, {self.Computer.process}, {self.Computer.memory}")
        print(f"{self.name}", "=>", self.Computer.model, self.Computer.process, self.Computer.memory)

    def __str__(self):
        return f"({self.Computer.model}, {self.Computer.process}, {self.Computer.memory})"

    class Computer:
        # def __init__(self, model, process, memory):
        #     # self.Computer_inner = self.ComputerClass()
        #     self._model = model
        #     self._process = process
        #     self._memory = memory
        def model(self):
            # pass
            return "HP"
        #     self.model= "HP"
        #     return self.model
        #
        def process(self):
            return "i7"
            # pass
        def memory(self):
            return 16
            # pass
outer = Student("Roman")
# outer.print_info()
# outer.__str__()
# print(outer)
# print(outer)
outer = Student("Vladimir")
# print(outer)


# outer.show()
 # class Geekforgeeks:
#     def __init__(self):
#            self.inner = self.Inner()
#
#     def show(self):
#         print("This is an outer class")
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#         def show(self):
#             print("This is the inner class")
#
#         class InnerClass:
#             def show(self):
#                 print("This is the inner class in inner class")
#
# outer = Geekforgeeks()
# outer.show()
#
# inner1 = outer.inner
# inner1.show()
#
# inner2 = outer.inner.inner_inner
# inner2.show()


#
#     class OS:
#         def system(self):
#             return "Windows 10"
#
#
#     class CPU:
#         def make(self):
#             return "Intel"
#
#         def model(self):
#             return "Core -i7"
#
# comp = Computer()
# my_os = comp.os
# my_cpu=comp.cpu
#
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())