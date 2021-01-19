from asteroid import Vector, Asteroid
import random
import datetime
import time


class Controller:
    def __init__(self):
        self._list_of_asteroids = []
        for x in range(100):
            position_vector = Vector(random.randint(0, 101), random.randint(0, 101), random.randint(0, 101))
            velocity_vector = Vector(random.randint(0, 6), random.randint(0, 6), random.randint(0, 6))
            new_asteroid = Asteroid(Asteroid.calculate_circumference(random.randint(1, 5)),
                                    position_vector, velocity_vector)
            self._list_of_asteroids.append(new_asteroid)

    def simulate(self, seconds: int):
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
