# Real-Time E-Commerce Data Warehouse

## Overview

This project simulates a real-time e-commerce platform that ingests customer events through Apache Kafka, processes them using Apache Spark Structured Streaming, stores historical data in Snowflake using a Star Schema with Slowly Changing Dimensions (SCD Type 2), and visualizes business metrics in Power BI.

## Tech Stack

- Python
- Apache Kafka
- Apache Spark
- Snowflake
- AWS S3
- Airflow
- dbt
- Docker
- Power BI

## Project Flow

Python Event Generator
        ↓
Kafka
        ↓
Spark Streaming
        ↓
Snowflake
        ↓
dbt
        ↓
Dashboard