# Kafka Stock Analysis Pipeline

## Introduction
This project demonstrates the implementation of a complex data pipeline using Apache Kafka, MongoDB, and Python. The primary objective is to process stock data for Microsoft and Apple, analyze it through various consumers, and store the results in MongoDB. This pipeline showcases how real-time data processing and analysis can be achieved using Kafka's robust messaging system.

## Objective
The main objectives of this project are:
1. To set up a Kafka cluster with multiple brokers and topics.
2. To create producers that send stock data for Microsoft and Apple to Kafka topics.
3. To develop consumers that process the stock data in different ways:
   - Calculate the difference between opening and closing prices.
   - Determine the risk based on the high and low prices.
   - Compute the daily percentage change in stock prices.
4. To store the processed data in MongoDB for further analysis.

## Methodologies
1. **Setting up Kafka Cluster**: Initialize a Kafka cluster with three brokers and configure topics with appropriate replication factors and retention periods.
2. **Data Production**: Use producers to fetch and send stock data for Microsoft and Apple to Kafka topics.
3. **Data Consumption and Processing**: Implement consumers to process the stock data:
   - **Consumer1**: Calculate the difference between opening and closing prices.
   - **Consumer2**: Assess the risk based on high and low price differences.
   - **Consumer3**: Compute the daily percentage change in stock prices.
4. **Data Storage**: Store the results in MongoDB collections for each type of processed data.

## Technologies Used
- **Apache Kafka**: For setting up the data pipeline with producers and consumers.
- **Python**: For writing producer and consumer scripts.
- **MongoDB**: For storing processed data.
- **PyCharm**: Integrated Development Environment for developing the scripts.
- **MongoDB Compass**: GUI tool for MongoDB to view and manage databases.

## How to Run

### Prerequisites
- Install Kafka and MongoDB on your system.
- Ensure you have Python and PyCharm installed.

### Steps
1. **Start Zookeeper**:
   ```sh
   zookeeper-server-start.sh config/zookeeper.properties
   ```
2. **Start Kafka Brokers**:
   Run each command in a separate terminal.
   ```
   kafka-server-start.sh config/server-1.properties
   kafka-server-start.sh config/server-2.properties
   kafka-server-start.sh config/server-3.properties

3. **Start MongoDB**:
   ```
   sudo systemctl start mongod
   sudo systemctl status mongod
   ```
4. **Run Python Scripts**:
   Open the following files in PyCharm:
   - producer1.py
   - producer2.py
   - consumer1.py
   - consumer2.py
   - consumer3.py
   - Execute producer1.py and producer2.py first to start producing data.
   - Execute consumer1.py, consumer2.py, and consumer3.py to start consuming and processing data.

## Conclusion
This project demonstrates the integration of Apache Kafka and MongoDB to build a real-time data processing pipeline. By analyzing stock data for Microsoft and Apple, the pipeline offers insights into price changes, risk assessment, and percentage fluctuations, stored in MongoDB for further analysis.


 
 
