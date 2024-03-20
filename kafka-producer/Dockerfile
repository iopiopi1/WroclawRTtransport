FROM python:3.10

WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

ENV kafka_bootstrap_server="34.118.234.37:9092"
ENV target_url="https://www.wroclaw.pl/open-data/api/action/datastore_search?resource_id=17308285-3977-42f7-81b7-fdd168c210a2&offset={offset}&limit={limit}"
ENV topic_name="mpk-wroclaw-location"

CMD [ "python", "./main.py"]