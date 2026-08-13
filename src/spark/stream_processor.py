"""
Spark Structured Streaming Consumer

Kafka -> Spark -> S3 Bronze
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    current_timestamp,
    to_date,
)


KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"
KAFKA_TOPIC = "events"

S3_BUCKET = "abhinav-ecommerce-data-lake"

S3_BRONZE_PATH = (
    f"s3a://{S3_BUCKET}/bronze/ecommerce_events/"
)

S3_CHECKPOINT_PATH = (
    f"s3a://{S3_BUCKET}/checkpoints/ecommerce_bronze/"
)


def create_spark_session() -> SparkSession:

    return (
        SparkSession.builder
        .appName("EcommerceKafkaToS3Bronze")
        .master("local[*]")
        .config(
            "spark.hadoop.fs.s3a.impl",
            "org.apache.hadoop.fs.s3a.S3AFileSystem",
        )
        .config(
            "spark.hadoop.fs.s3a.aws.credentials.provider",
            "software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider",
        )
        .config(
            "spark.hadoop.fs.s3a.endpoint",
            "s3.ap-southeast-2.amazonaws.com",
        )
        .getOrCreate()
    )


def create_kafka_stream(
    spark: SparkSession,
):

    return (
        spark.readStream
        .format("kafka")
        .option(
            "kafka.bootstrap.servers",
            KAFKA_BOOTSTRAP_SERVERS,
        )
        .option(
            "subscribe",
            KAFKA_TOPIC,
        )
        .option(
            "startingOffsets",
            "latest",
        )
        .load()
    )


def create_bronze_dataframe(
    kafka_df,
):

    return (
        kafka_df
        .select(
            col("timestamp").alias(
                "kafka_timestamp"
            ),
            col("partition").alias(
                "kafka_partition"
            ),
            col("offset").alias(
                "kafka_offset"
            ),
            col("value")
            .cast("string")
            .alias("raw_event"),
        )
        .withColumn(
            "ingestion_timestamp",
            current_timestamp(),
        )
        .withColumn(
            "event_date",
            to_date(
                col("kafka_timestamp")
            ),
        )
    )


def main():

    spark = create_spark_session()

    spark.sparkContext.setLogLevel(
        "WARN"
    )

    kafka_df = create_kafka_stream(
        spark
    )

    bronze_df = create_bronze_dataframe(
        kafka_df
    )

    query = (
        bronze_df
        .writeStream
        .format("parquet")
        .outputMode("append")
        .option(
            "path",
            S3_BRONZE_PATH,
        )
        .option(
            "checkpointLocation",
            S3_CHECKPOINT_PATH,
        )
        .partitionBy(
            "event_date"
        )
        .trigger(
            processingTime="10 seconds"
        )
        .start()
    )

    query.awaitTermination()


if __name__ == "__main__":
    main()