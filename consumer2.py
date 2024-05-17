#CALCULATE HIGHEST STOCK PRICE
from kafka import KafkaConsumer
import pymongo 
import json
stockPRiceDict={'AAPL':{'high':0 },'MSFT':{'high':0 }}

bootstrap_servers = ["localhost:9093","localhost:9094","localhost:9095"]
client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
consumer=KafkaConsumer("STOCK_OF_MICROSOFT","STOCK_OF_APPLE",bootstrap_servers=bootstrap_servers, value_deserializer=lambda m: json.loads(m.decode('utf-8')))

DATA_BASE=client.kafka_consumer_database
collection=DATA_BASE.HIGHLOWPRICE
for producer_message in consumer:
    prices=float(producer_message.value['05. price'])
    symbols=producer_message.value['01. symbol']

    stockPRiceDict[symbols]['high']=max(stockPRiceDict[symbols]['high'],prices)
    
    print(f"HIGH PRICE OF {symbols} IS {stockPRiceDict[symbols]['high']}")   
    collection.update_one({'symbol':symbols},{'$set':{'high': stockPRiceDict[symbols]['high']}}, upsert=True)
