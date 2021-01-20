import math


class Vector:
    """
    This class represents a mathematical vector that stores an x, y and z values measured in metres.
    """
    def __init__(self, x: int or float, y: int or float, z: int or float):
        """
        Initializes a Vector object with x, y and z attributes measured in metres.

        :param x: value at x in metres
        :param y: value at y in metres
        :param z: value at z in metres
        :precondition: x must be an integer or float
        :precondition: y must be an integer or float
        :precondition: z must be an integer or float
        """
        self._x = x
        self._y = y
        self._z = z

    def get_x(self):
        """
        Gets the x attribute.

        :return: The x attribute
        """
        return self._x

    def get_y(self):
        """
        Gets the y attribute.

        :return: The y attribute
        """
        return self._y

    def get_z(self):
        """
        Gets the z attribute.

        :return: The z attribute
        """
        return self._z

    def set_x(self, x):
        """
        Sets the x attribute.

        :param x: The value to change x to.
        :precondition: x must be an integer or float.
        """
        self._x = x

    def set_y(self, y):
        """
        Sets the y attribute.

        :param y: The value to change y to.
        :precondition: y must be an integer or float.
        """
        self._y = y

    def set_z(self, z):
        """
        Sets the z attribute.

        :param z: The value to change z to.
        :precondition: z must be an integer or float.
        """
        self._z = z

    def add(self, vector):
        """
        Adds two vector together.

        :param vector: The vector to be added.
        :precondition: vector must be a vector class.
        """
        self.set_x(self._x + vector.get_x())
        self.set_y(self._y + vector.get_y())
        self.set_z(self._z + vector.get_z())

    def return_as_tuple(self):
        """
        Returns the vector represented as a tuple.

        :return: The vector represented as a tuple.
        """
        return tuple((self._x, self._y, self._z))

    def __str__(self):
        """
        Prints the vector as a string.
        """
        print(f"{self.return_as_tuple()}")


class Asteroid:
    """
    This class represents an Asteroid that has a circumference and a position and velocity stored as Vectors. Each
    Asteroid has a unique ID.
    """
    asteroid_id = 1

    def __init__(self, circumference: int or float, position: Vector, velocity: Vector):
        """
        Initializes an Asteroid object with a circumference, position and velocity. Will increment the id of the
        Asteroid on each initialization as well.

        :param circumference: The circumference of the Asteroid.
        :param position: The current position of the Asteroid in metres.
        :param velocity: The current velocity of the Asteroid in metres.
        """
        self.circumference = circumference
        self._position = position
        self._velocity = velocity
        self.__id = Asteroid.asteroid_id
        Asteroid.increment_id()

    def get_circumference(self):
        """
        Gets the circumference.

        :return: The circumference.
        """
        return self.circumference

    def get_position(self):
        """
        Gets the position of the Asteroid.

        :return: The position of the Asteroid,
        """
        return self._position

    def get_velocity(self):
        """
        Gets the velocity of the Asteroid.

        :return: The velocity of the Asteroid.
        """
        return self._velocity

    def get_id(self):
        """
        Gets the id of the Asteroid.

        :return: The id of the Asteroid.
        """
        return self.__id

    def set_circumference(self, circumference):
        """
        Sets the circumference.

        :param circumference: The value of the circumference to be set to.
        :precondition: circumference must be an integer or float.
        """
        self.circumference = circumference

    def set_position(self, position):
        """
        Sets the position of the Asteroid.

        :param position: The value of the position to be set to.
        :precondition: position must be a vector.
        """
        self._position = position

    def set_velocity(self, velocity):
        """
        Sets the velocity of the Asteroid.

        :param velocity: The value of the velocity to be set to.
        :precondition: velocity must be a vector.
        """
        self._velocity = velocity

    def move(self):
        """
        Moves the Asteroid based on its velocity.

        :return: The Asteroid's new position.
        """
        self._position.add(self._velocity)
        return self._position.return_as_tuple()

    @classmethod
    def increment_id(cls):
        """
        Increments the Asteroid's id.
        """
        Asteroid.asteroid_id += 1

    @staticmethod
    def calculate_circumference(radius: int or float):
        """
        Calculates the circumference of the Asteroid using a radius.

        :param radius: The radius to be used to calculate the circumference.
        :precondition: The radius must be a number (int or float).
        :return: The calculated circumference.
        """
        return 2 * math.pi * radius

    def __str__(self):
        """
        Prints the Asteroid object's attributes as a string.
        """
        print(f"Circumference is: {self.circumference}, position is: {self._position.__str__()}, velocity is: "
              f"{self._velocity.__str__()}")
