import logging

from kafka import KafkaProducer
from kafka.errors import KafkaError
from requests import get
from typing import List
from requests.exceptions import HTTPError, JSONDecodeError
import json
import os
import time



class MPKParser:
    def __init__(self, producer_id: int, limit: int = 100):
        logging.info('Started process')
        self.producer_id = producer_id
        self.limit = limit
        self.producer = KafkaProducer(
            bootstrap_servers=['localhost:29092'],
            api_version=(7, 6, 0),
            compression_type='gzip',
            batch_size=100,
            acks=1

        )

    def request(self):
        try:
            offset = 0
            url_raw = os.getenv('target_url')
            url = url_raw.format(offset=offset, limit=self.limit)
            topic_name = os.getenv('topic_name')

            while True:
                counter = 100
                while counter >= self.limit:
                    counter = 0
                    response = get(url=url, timeout=10)
                    response.raise_for_status()
                    r = response.json()
                    for location in r.get('result').get('records'):
                        counter += 0
                        self.producer.send(
                            topic=topic_name,
                            value=json.dumps(location).encode('ascii')
                        )
                    offset += self.limit
                # if all processed - sleep for 10 secs
                time.sleep(10)
        except (HTTPError, JSONDecodeError) as e:
            print(f"HTTP Error, {e}")


def parse(self):
        pass


