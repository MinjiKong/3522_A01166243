from asteroid import Vector, Asteroid
import random
import datetime
import time


class Controller:
    """
    This class is the controller for simulation of the Asteroids.
    """
    def __init__(self):
        """
        Initializes the Controller object with a list of randomly generated Asteroids.
        """
        self._list_of_asteroids = []
        for x in range(100):
            self._list_of_asteroids.append(Controller.create_asteroid(position_range=random.randint(0, 101),
                                                                      velocity_range=random.randint(0, 6),
                                                                      radius_range=random.randint(1, 5)))

    @classmethod
    def create_asteroid(cls, position_range: int or float, velocity_range: int or float, radius_range: int or float):
        """
        Creates an Asteroid with set values for each attribute.

        :param position_range: The range that the position vector will be generated with.
        :param velocity_range: The range that the velocity vector will be generated with.
        :param radius_range: The range that the radius will be generated with.
        :precondition: The position_range must be a number (int or float).
        :precondition: The velocity_range must be a number (int or float).
        :precondition: The radius must be a number (int or float).
        :return:
        """
        position_vector = Vector(position_range, position_range, position_range)
        velocity_vector = Vector(velocity_range, velocity_range, velocity_range)
        return Asteroid(Asteroid.calculate_circumference(radius_range),
                        position_vector, velocity_vector)

    def simulate(self, seconds: int):
        """
        Simulates Asteroids moving for the amount of seconds that is inputted.

        :param seconds: The amount of time the simulation is to be run.
        :precondition: The seconds must be a number (int or float).
        """
        for time_to_run in range(seconds):
            time.sleep(1 - datetime.datetime.now().microsecond * 0.000001)
            print(f"Simulation Start Time: {datetime.datetime.now()}\n")
            print("Moving Asteroids!\n---------------")
            for index, asteroid in enumerate(self._list_of_asteroids):
                print(f"Asteroid {asteroid.get_id()} Moved! Old Position {asteroid.get_position().return_as_tuple()} "
                      f"-> New Position {asteroid.move()}")

                print(f"Asteroid {asteroid.get_id()} is currently at {asteroid.get_position().get_x()}, "
                      f"{asteroid.get_position().get_y()}, {asteroid.get_position().get_z()} "
                      f"and moving at {asteroid.get_velocity().get_x()}, "
                      f"{asteroid.get_velocity().get_y()}, {asteroid.get_velocity().get_z()}. "
                      f"It has a circumference of {asteroid.get_circumference()}.\n")


if __name__ == "__main__":
    new_controller = Controller()
    new_controller.simulate(5)
