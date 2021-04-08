import threading
import time
import logging

from city_processor import CityOverheadTimes, ISSDataRequest, CityDatabase


class CityOverheadTimeQueue:
    """
    Class that represents a queue of Cities
    """
    def __init__(self):
        self.__data_queue = []
        self.access_queue_lock = threading.Lock()

    def put(self, overhead_time: CityOverheadTimes) -> None:
        """
        Puts a CityOverheadTime into the queue at the very back of the queue.
        :param overhead_time: CityOverheadTimes
        :return: None
        """
        self.__data_queue.append(overhead_time)

    def get(self) -> CityOverheadTimes:
        """
        Returns the first CityOverheadTimes object in the data queue. Deletes that entry from the queue
        :return: The first CityOverheadTimes in the queue.
        """
        first_item = self.__data_queue[0]
        del self.__data_queue[0]
        return first_item

    def __len__(self):
        return len(self.__data_queue)


class ProducerThread(threading.Thread):
    """
    Class that represents a thread that adds Cities to a queue.
    """
    def __init__(self, cities: list, queue: CityOverheadTimeQueue):
        super().__init__()
        self.cities = cities
        self.queue = queue

    def run(self) -> None:
        """
        Runs the thread. This thread should add cities from stored list to the queue and will wait for 1 second after
        reading a 5th city.
        :return: None
        """
        with self.queue.access_queue_lock:
            cities_counted = 0
            for city in self.cities:
                self.queue.put(ISSDataRequest.get_overhead_pass(city))
                cities_counted += 1
                if cities_counted % 5 == 0:
                    time.sleep(1)


class ConsumerThread(threading.Thread):
    """
    Class that represents a thread that gets Cities from the queue and prints them.
    """
    def __init__(self, queue: CityOverheadTimeQueue):
        super().__init__()
        self.queue = queue
        self.data_incoming = True

    def run(self) -> None:
        """
        Runs the thread. While there is data and the queue is > 0.
        This thread gets cities from the queue and prints them. It sleeps for 0.5 seconds after each
        print and once the queue empty, it sleeps for 0.75 seconds.
        """
        with self.queue.access_queue_lock:
            while self.data_incoming or self.queue.__len__() > 0:
                print(self.queue.get())
                print("\n")
                time.sleep(0.5)
                if self.queue.__len__() == 0:
                    time.sleep(0.75)
                    self.data_incoming = False


def main():
    start_time = time.time()
    queue = CityOverheadTimeQueue()

    # producer_one = ProducerThread(CityDatabase("city_locations_test.xlsx").city_db, queue)
    producer_two = ProducerThread(CityDatabase("city_locations.xlsx").city_db, queue)
    # I split up the cities in city_locations into two different excel files
    producer_three = ProducerThread(CityDatabase("city_location_other_half.xlsx").city_db, queue)

    # producer_one.run()
    producer_two.run()
    producer_three.run()

    consumer = ConsumerThread(queue)
    consumer.run()

    print(f"Program Duration: {time.time() - start_time} seconds")


if __name__ == "__main__":
    main()
