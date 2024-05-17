from kafka import KafkaProducer
import requests
import json
import time

bootstrap_servers = ["localhost:9093","localhost:9094","localhost:9095"]
producer = KafkaProducer(bootstrap_servers=bootstrap_servers, value_serializer=lambda m: json.dumps(m).encode('utf-8'))

url=f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=MSFT&apikey=VMANK1SUI8B7VTY4'
while True:
    response = requests.get(url)
    data = response.json()
    if 'Global Quote' in data:
         message=data['Global Quote']
         producer.send("STOCK_OF_MICROSOFT",value =message)
         print(f"PRODUCER   SENT MICROSOFT STOCK   {data['Global Quote']}")
    time.sleep(20)     

