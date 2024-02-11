import logging

from kafka import KafkaProducer
from kafka.errors import KafkaError
from requests import get
from typing import List
from requests.exceptions import HTTPError, JSONDecodeError
import json


class MPKParser:
    def __init__(self, producer_id: int, offset: int, limit: int = 100):
        logging.info('Started process')
        self.url = f'https://www.wroclaw.pl/open-data/api/action/datastore_search?resource_id=17308285-3977-42f7-81b7-fdd168c210a2&offset={offset}&limit={limit}'
        self.producer_id = producer_id
        self.producer = KafkaProducer(bootstrap_servers=['localhost:29092'], api_version=(7, 6, 0))

    def request(self):
        try:
            response = get(url=self.url, timeout=10)
            response.raise_for_status()
            r = response.json()
            self.producer.send(topic='mpk-wroclaw-location', value=json.dumps(r).encode('ascii'))
            print(r)
        except (HTTPError, JSONDecodeError) as e:
            print(f"HTTP Error, {e}")


def parse(self):
        pass


