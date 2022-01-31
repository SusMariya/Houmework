class NonPoint:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __set__(self, instance, value):
        if type(value) != int:
            raise ValueError("Значение должно целым")
        print(f"__set__: {self.name} = {value}")
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class Point3D:
    x = NonPoint()
    y = NonPoint()
    z = NonPoint()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p = Point3D(1, 2, 3)
print(p.__dict__)
