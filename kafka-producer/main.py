from TransportLocationProducer import MPKParser
from multiprocessing import Process


def start(worker_number: int = 7):
    pool = []

    for offset in range(worker_number):
        p = Process(
            target=start_producer,
            kwargs={
                'limit': 100,
                'offset': offset,
                'producer_id': offset
            })
        p.start()
        pool.append(p)


def start_producer(offset: int, producer_id: int, limit: int):
    producer = MPKParser(producer_id=producer_id, offset=offset, limit=limit)
    producer.request()
    return producer


if __name__ == '__main__':
    start()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
