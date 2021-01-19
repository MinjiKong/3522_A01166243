import math


class Vector:
    def __init__(self, x: int or float, y: int or float, z: int or float):
        self._x = x
        self._y = y
        self._z = z

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_z(self):
        return self._z

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def set_z(self, z):
        self._z = z

    def add(self, vector):
        print("adding vectors")
        self.set_x(self._x + vector.get_x())
        self.set_y(self._y + vector.get_y())
        self.set_z(self._z + vector.get_z())

    def return_as_tuple(self):
        return tuple((self._x, self._y, self._z))

    def __str__(self):
        print(self.return_as_tuple())


class Asteroid:
    asteroid_id = 1

    def __init__(self, circumference: int or float, position: Vector, velocity: Vector):
        self.circumference = circumference
        self._position = position
        self._velocity = velocity
        self._id = Asteroid.asteroid_id
        Asteroid.increment_id()

    def get_circumference(self):
        return self.circumference

    def get_position(self):
        return self._position

    def get_velocity(self):
        return self._velocity

    def get_id(self):
        return self._id

    def set_circumference(self, circumference):
        self.circumference = circumference

    def set_position(self, position):
        self._position = position

    def set_velocity(self, velocity):
        self._velocity = velocity

    def move(self):
        self._position.add(self._velocity)
        return self._position.return_as_tuple()

    @classmethod
    def increment_id(cls):
        Asteroid.asteroid_id += 1

    @staticmethod
    def calculate_circumference(radius):
        return 2 * math.pi * radius

    def __str__(self):
        print(f"Circumference is: {self.circumference}, position is: {self._position.__str__()}, velocity is: "
              f"{self._velocity.__str__()}")
