from kafka import KafkaConsumer
import pymongo
import json

stockPriceDict = {'AAPL': {'percent': []}, 'MSFT': {'percent': []}}

bootstrap_servers = ["localhost:9093", "localhost:9094", "localhost:9095"]
client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
consumer = KafkaConsumer("STOCK_OF_MICROSOFT", "STOCK_OF_APPLE", bootstrap_servers=bootstrap_servers,value_deserializer=lambda m: json.loads(m.decode('utf-8')))

DATA_BASE = client.kafka_consumer_database
collection = DATA_BASE.PERCENT_CHANGE
for producer_message in consumer:
    prices = float(producer_message.value['08. previous close'])
    op = float(producer_message.value['02. open'])
    symbols = producer_message.value['01. symbol']
    percent_change = ((op - prices) / prices) * 100

    stockPriceDict[symbols]['percent'].append(percent_change)
    if percent_change > 0:
        print(f"The daily percentage change in {symbols} is {percent_change:.2f} the stock has experienced a increase in its price compared to the previous trading day. ")
    if percent_change < 0:
        print(f"The daily percentage change in {symbols} is {percent_change:.2f} the stock has experienced a decrease in its price compared to the previous trading day. ")
    collection.update_one({'symbol': symbols}, {'$set': {'Percent Change': stockPriceDict[symbols]['percent']}},upsert=True)



