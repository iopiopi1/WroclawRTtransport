from TransportLocationProducer import MPKParser



# url =f'https://www.wroclaw.pl/open-data/api/action/datastore_search?resource_id=17308285-3977-42f7-81b7-fdd168c210a2&offset={offset}&limit={limit}'

# mpk-wroclaw-location

#url = os.getenv('target_url')
#topic_name = os.getenv('topic_name')

def start():
    producer = MPKParser(producer_id=1, limit=100)
    producer.request()


if __name__ == '__main__':
    start()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
