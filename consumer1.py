from kafka import KafkaConsumer
import pymongo 
import json
stockPRiceDict={'MSFT':[],'AAPL':[]}

bootstrap_servers = ["localhost:9093","localhost:9094","localhost:9095"]
client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
consumer=KafkaConsumer("STOCK_OF_MICROSOFT","STOCK_OF_APPLE",bootstrap_servers=bootstrap_servers, value_deserializer=lambda m: json.loads(m.decode('utf-8')))

DATA_BASE=client.kafka_consumer_database
collection=DATA_BASE.AveragePrice
for producer_message in consumer:
    prices=float(producer_message.value['05. price'])
    symbols=producer_message.value['01. symbol']
    stockPRiceDict[symbols].append(prices)
    average=sum(stockPRiceDict[symbols])/len(stockPRiceDict[symbols])
    print(f"AVERAGE PRICE OF {symbols} IS {average:.2f}")





