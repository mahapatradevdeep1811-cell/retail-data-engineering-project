Retail Data Engineering Project
Project Overview

This project demonstrates an end-to-end Data Engineering pipeline built using modern enterprise technologies including Python, PostgreSQL, Docker, and Apache Kafka.

The project simulates a real-world retail analytics platform capable of handling both:

Batch ETL Processing
Real-Time Streaming Data Processing

The architecture follows enterprise-style data engineering workflows commonly used in modern cloud and analytics platforms.

Architecture
                    +------------------+
                    |   CSV Datasets   |
                    +------------------+
                              |
                              v
                    +------------------+
                    | Python Batch ETL |
                    +------------------+
                              |
                              v
                    +------------------+
                    |   PostgreSQL DW  |
                    +------------------+

------------------------------------------------------

              REAL-TIME STREAMING PIPELINE

                    +------------------+
                    | Kafka Producer   |
                    +------------------+
                              |
                              v
                    +------------------+
                    |   Kafka Topic    |
                    +------------------+
                              |
                              v
                    +------------------+
                    | Kafka Consumer   |
                    +------------------+
                              |
                              v
                    +------------------+
                    | PostgreSQL Table |
                    +------------------+
Technologies Used
Technology	Purpose
Python	ETL & Streaming Logic
PostgreSQL	Data Warehouse
Docker	Containerization
Apache Kafka	Real-Time Streaming
Pandas	Data Transformation
SQLAlchemy	Database Connectivity
psycopg2	PostgreSQL Integration
Git & GitHub	Version Control
VS Code	Development Environment
Project Features
Batch ETL Pipeline
Reads retail datasets from CSV files
Performs data transformation and joins
Calculates revenue metrics
Loads transformed data into PostgreSQL
Data Validation

Implemented data quality checks for:

Null values
Duplicate records
Negative quantity validation
Logging & Monitoring

Implemented operational logging using Python logging module.

Features:

INFO logs
ETL execution tracking
Operational monitoring
Dockerized Deployment

Containerized ETL workflows using Docker for:

Environment consistency
Portable deployment
Enterprise-style execution
Real-Time Streaming Pipeline

Implemented Kafka-based streaming architecture:

Kafka Producer
Kafka Consumer
Real-time transaction ingestion
Streaming data load into PostgreSQL
Project Structure
gcp-retail-data-engineering-project/
│
├── batch/
│   ├── batch_etl.py
│   ├── data_validation.py
│   └── pyspark_etl.py
│
├── streaming/
│   ├── producer.py
│   └── consumer.py
│
├── sql/
│   └── analytics_queries.sql
│
├── data/
│   ├── customers.csv
│   ├── products.csv
│   └── orders.csv
│
├── logs/
│   └── etl.log
│
├── screenshots/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore
Setup Instructions
Clone Repository
git clone https://github.com/mahapatradevdeep1811-cell/retail-data-engineering-project
Create Virtual Environment
python -m venv venv

Activate environment:

Windows
.\venv\Scripts\activate
Install Dependencies
pip install -r requirements.txt
Running Batch ETL Pipeline
python batch/batch_etl.py
Running Kafka Streaming Pipeline
Start Kafka Containers
docker compose up -d
Run Consumer
python streaming/consumer.py
Run Producer
python streaming/producer.py
Sample SQL Query
SELECT * FROM sales_data;
Key Learning Outcomes
ETL Pipeline Development
Real-Time Streaming Architecture
Kafka Producer-Consumer Model
Docker Containerization
PostgreSQL Data Warehousing
Data Validation & Monitoring
Enterprise Debugging & Troubleshooting
Distributed Systems Fundamentals
Future Enhancements
Apache Airflow Orchestration
CI/CD Pipeline Integration
Cloud Deployment (AWS/GCP/Azure)
Monitoring Dashboards
PySpark Distributed Processing
Data Lake Integration

Author
Devdeep Mahapatra