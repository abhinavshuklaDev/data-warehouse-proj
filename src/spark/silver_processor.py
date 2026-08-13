"""
Silver Layer Processor

Reads raw Bronze events from S3,
parses the JSON payload, standardizes
data types, and writes structured
Silver data back to S3.
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    from_json,
    to_timestamp,
)
from pyspark.sql.types import (
    DateType,
    DoubleType,
    IntegerType,
    LongType,
    StringType,
    StructField,
    StructType,
    TimestampType,
)

from pyspark.sql.types import (
    DoubleType,
    IntegerType,
    StringType,
    StructField,
    StructType,
)


S3_BUCKET = "abhinav-ecommerce-data-lake"

S3_BRONZE_PATH = (
    f"s3a://{S3_BUCKET}/bronze/ecommerce_events/"
)

S3_SILVER_PATH = (
    f"s3a://{S3_BUCKET}/silver/ecommerce_events/"
)

S3_CHECKPOINT_PATH = (
    f"s3a://{S3_BUCKET}/checkpoints/ecommerce_silver/"
)


# ---------------------------------------------------------
# Bronze file schema
# ---------------------------------------------------------

BRONZE_SCHEMA = StructType(
    [
        StructField(
            "kafka_timestamp",
            StringType(),
            True,
        ),
        StructField(
            "kafka_partition",
            IntegerType(),
            True,
        ),
        StructField(
            "kafka_offset",
            LongType(),
            True,
        ),
        StructField(
            "raw_event",
            StringType(),
            True,
        ),
        StructField(
            "ingestion_timestamp",
            TimestampType(),
            True,
        ),
        StructField(
            "event_date",
            DateType(),
            True,
        ),
    ]
)


# ---------------------------------------------------------
# Event JSON schema
# ---------------------------------------------------------

EVENT_SCHEMA = StructType(
    [
        StructField(
            "event_id",
            StringType(),
            True,
        ),
        StructField(
            "event_type",
            StringType(),
            True,
        ),
        StructField(
            "event_timestamp",
            StringType(),
            True,
        ),
        StructField(
            "customer_id",
            StringType(),
            True,
        ),
        StructField(
            "product_id",
            StringType(),
            True,
        ),
        StructField(
            "session_id",
            StringType(),
            True,
        ),
        StructField(
            "source",
            StringType(),
            True,
        ),

        # Cart
        StructField(
            "cart_id",
            StringType(),
            True,
        ),
        StructField(
            "quantity",
            IntegerType(),
            True,
        ),
        StructField(
            "unit_price",
            DoubleType(),
            True,
        ),
        StructField(
            "cart_total",
            DoubleType(),
            True,
        ),

        # Order
        StructField(
            "order_id",
            StringType(),
            True,
        ),
        StructField(
            "warehouse_id",
            StringType(),
            True,
        ),
        StructField(
            "supplier_id",
            StringType(),
            True,
        ),
        StructField(
            "total_amount",
            DoubleType(),
            True,
        ),
        StructField(
            "order_status",
            StringType(),
            True,
        ),

        # Payment
        StructField(
            "payment_id",
            StringType(),
            True,
        ),
        StructField(
            "payment_method",
            StringType(),
            True,
        ),
        StructField(
            "payment_status",
            StringType(),
            True,
        ),
        StructField(
            "transaction_amount",
            DoubleType(),
            True,
        ),

        # Inventory
        StructField(
            "inventory_id",
            StringType(),
            True,
        ),
        StructField(
            "quantity_reserved",
            IntegerType(),
            True,
        ),
        StructField(
            "remaining_stock",
            IntegerType(),
            True,
        ),
        StructField(
            "inventory_status",
            StringType(),
            True,
        ),

        # Return
        StructField(
            "return_id",
            StringType(),
            True,
        ),
        StructField(
            "reason",
            StringType(),
            True,
        ),
        StructField(
            "refund_amount",
            DoubleType(),
            True,
        ),
        StructField(
            "return_status",
            StringType(),
            True,
        ),
    ]
)


def create_spark_session() -> SparkSession:

    return (
        SparkSession.builder
        .appName(
            "EcommerceBronzeToSilver"
        )
        .master("local[*]")
        .config(
            "spark.hadoop.fs.s3a.impl",
            "org.apache.hadoop.fs.s3a.S3AFileSystem",
        )
        .config(
            "spark.hadoop.fs.s3a.aws.credentials.provider",
            (
                "software.amazon.awssdk.auth.credentials."
                "ProfileCredentialsProvider"
            ),
        )
        .config(
            "spark.hadoop.fs.s3a.endpoint",
            "s3.ap-southeast-2.amazonaws.com",
        )
        .getOrCreate()
    )


def read_bronze_stream(
    spark: SparkSession,
):

    return (
        spark.readStream
        .schema(BRONZE_SCHEMA)
        .format("parquet")
        .load(
            S3_BRONZE_PATH
        )
    )


def parse_raw_events(
    bronze_df,
):

    parsed_df = bronze_df.select(
        "*",
        from_json(
            col("raw_event"),
            EVENT_SCHEMA,
        ).alias("event"),
    )

    return parsed_df.select(
        "event.*",
        "kafka_timestamp",
        "kafka_partition",
        "kafka_offset",
        "ingestion_timestamp",
        "event_date",
    )


def standardize_events(
    events_df,
):

    return (
        events_df
        .withColumn(
            "event_timestamp",
            to_timestamp(
                col("event_timestamp")
            ),
        )
        .filter(
            col("event_id").isNotNull()
        )
        .filter(
            col("event_type").isNotNull()
        )
        .filter(
            col("event_timestamp").isNotNull()
        )
    )


def main():

    spark = create_spark_session()

    spark.sparkContext.setLogLevel(
        "WARN"
    )

    bronze_df = read_bronze_stream(
        spark
    )

    parsed_df = parse_raw_events(
        bronze_df
    )

    silver_df = standardize_events(
        parsed_df
    )

    query = (
        silver_df
        .writeStream
        .format("parquet")
        .outputMode("append")
        .option(
            "path",
            S3_SILVER_PATH,
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