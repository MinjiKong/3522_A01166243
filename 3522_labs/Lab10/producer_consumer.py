import threading
import time
import asyncio

from city_processor import CityOverheadTimes, City, ISSDataRequest


class CityOverheadTimeQueue:
    def __init__(self):
        self.__data_queue = []
        self.access_queue_lock = threading.Lock()

    def put(self, overhead_time: CityOverheadTimes) -> None:
        self.__data_queue.append(overhead_time)

    def get(self) -> CityOverheadTimes:
        first_item = self.__data_queue[0]
        del self.__data_queue[0]
        return first_item

    def __len__(self):
        return len(self.__data_queue)


class ProducerThread(threading.Thread):
    def __init__(self, cities: list, queue: CityOverheadTimeQueue):
        super().__init__()
        self.cities = cities
        self.queue = queue

    def run(self) -> None:
        cities_read = 0
        for city in self.cities:
            ISSDataRequest.get_overhead_pass(city)
            cities_read += 1
            if cities_read % 5 == 0:
                time.sleep(1)


class ConsumerThread(threading.Thread):
    def __init__(self, queue: CityOverheadTimeQueue):
        super().__init__()
        self.queue = queue
        self.data_incoming = True

    def run(self) -> None:
        while self.data_incoming or self.queue.__len__() > 0:
            print(self.queue.get())
            time.sleep(0.5)
            if self.queue.__len__() == 0:
                time.sleep(0.75)


def main():
    city1 = City("Vancouver", 49.2734, -123.1216)
    city2 = City("Yellowknife", 62.442, -114.397)

    queue = CityOverheadTimeQueue()
    queue.put(ISSDataRequest.get_overhead_pass(city1).__str__())
    queue.put(ISSDataRequest.get_overhead_pass(city2).__str__())
    print(queue.__len__())
    print(queue.get())
    print(queue.__len__())


if __name__ == "__main__":
    main()
