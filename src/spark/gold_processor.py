"""
Gold Layer Processor

Creates business-oriented analytical datasets
from the Silver event layer.

Outputs:
    - Daily Sales
    - Customer Funnel
    - Product Performance
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    countDistinct,
    lit,
    sum,
    to_date,
    when,
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


S3_BUCKET = "abhinav-ecommerce-data-lake"

S3_SILVER_PATH = (
    f"s3a://{S3_BUCKET}/silver/ecommerce_events/"
)

S3_GOLD_SALES_PATH = (
    f"s3a://{S3_BUCKET}/gold/daily_sales/"
)

S3_GOLD_FUNNEL_PATH = (
    f"s3a://{S3_BUCKET}/gold/customer_funnel/"
)

S3_GOLD_PRODUCT_PATH = (
    f"s3a://{S3_BUCKET}/gold/product_performance/"
)


SILVER_SCHEMA = StructType(
    [
        StructField("event_id", StringType(), True),
        StructField("event_type", StringType(), True),
        StructField(
            "event_timestamp",
            TimestampType(),
            True,
        ),
        StructField("customer_id", StringType(), True),
        StructField("product_id", StringType(), True),
        StructField("session_id", StringType(), True),
        StructField("source", StringType(), True),

        StructField("cart_id", StringType(), True),
        StructField("quantity", IntegerType(), True),
        StructField("unit_price", DoubleType(), True),
        StructField("cart_total", DoubleType(), True),

        StructField("order_id", StringType(), True),
        StructField("warehouse_id", StringType(), True),
        StructField("supplier_id", StringType(), True),
        StructField("total_amount", DoubleType(), True),
        StructField("order_status", StringType(), True),

        StructField("payment_id", StringType(), True),
        StructField("payment_method", StringType(), True),
        StructField("payment_status", StringType(), True),
        StructField(
            "transaction_amount",
            DoubleType(),
            True,
        ),

        StructField("inventory_id", StringType(), True),
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

        StructField("return_id", StringType(), True),
        StructField("reason", StringType(), True),
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

        StructField(
            "kafka_timestamp",
            TimestampType(),
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


def create_spark_session() -> SparkSession:

    return (
        SparkSession.builder
        .appName(
            "EcommerceSilverToGold"
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


def read_silver(
    spark: SparkSession,
):

    return (
        spark.read
        .schema(SILVER_SCHEMA)
        .parquet(
            S3_SILVER_PATH
        )
    )


def build_daily_sales(
    silver_df,
):

    orders_df = (
        silver_df
        .filter(
            col("event_type") == "ORDER"
        )
        .filter(
            col("order_status") == "ORDER_CREATED"
        )
        .filter(
            col("order_id").isNotNull()
        )
    )

    return (
        orders_df
        .groupBy(
            to_date(
                col("event_timestamp")
            ).alias("sales_date")
        )
        .agg(
            countDistinct(
                "order_id"
            ).alias(
                "total_orders"
            ),
            countDistinct(
                "customer_id"
            ).alias(
                "unique_customers"
            ),
            sum(
                col("quantity")
            ).alias(
                "units_sold"
            ),
            sum(
                col("total_amount")
            ).alias(
                "gross_revenue"
            ),
        )
        .withColumn(
            "average_order_value",
            col("gross_revenue")
            / col("total_orders"),
        )
        .orderBy(
            "sales_date"
        )
    )


def build_customer_funnel(
    silver_df,
):

    session_events = (
        silver_df
        .filter(
            col("session_id").isNotNull()
        )
        .groupBy(
            "session_id"
        )
        .agg(
            countDistinct(
                when(
                    col("event_type")
                    == "PRODUCT_VIEW",
                    col("event_id"),
                )
            ).alias(
                "product_view_events"
            ),
            countDistinct(
                when(
                    col("event_type") == "CART",
                    col("event_id"),
                )
            ).alias(
                "cart_events"
            ),
            countDistinct(
                when(
                    col("event_type") == "ORDER",
                    col("event_id"),
                )
            ).alias(
                "order_events"
            ),
            countDistinct(
                when(
                    (
                        (col("event_type") == "PAYMENT")
                        & (
                            col("payment_status")
                            == "SUCCESS"
                        )
                    ),
                    col("event_id"),
                )
            ).alias(
                "successful_payment_events"
            ),
        )
    )

    return (
        session_events
        .agg(
            countDistinct(
                when(
                    col("product_view_events") > 0,
                    col("session_id"),
                )
            ).alias(
                "view_sessions"
            ),
            countDistinct(
                when(
                    col("cart_events") > 0,
                    col("session_id"),
                )
            ).alias(
                "cart_sessions"
            ),
            countDistinct(
                when(
                    col("order_events") > 0,
                    col("session_id"),
                )
            ).alias(
                "order_sessions"
            ),
            countDistinct(
                when(
                    col(
                        "successful_payment_events"
                    ) > 0,
                    col("session_id"),
                )
            ).alias(
                "successful_payment_sessions"
            ),
        )
        .withColumn(
            "cart_rate",
            when(
                col("view_sessions") > 0,
                col("cart_sessions")
                / col("view_sessions"),
            ).otherwise(lit(0.0)),
        )
        .withColumn(
            "order_rate",
            when(
                col("cart_sessions") > 0,
                col("order_sessions")
                / col("cart_sessions"),
            ).otherwise(lit(0.0)),
        )
        .withColumn(
            "payment_rate",
            when(
                col("order_sessions") > 0,
                col("successful_payment_sessions")
                / col("order_sessions"),
            ).otherwise(lit(0.0)),
        )
        .withColumn(
            "cart_abandonment_rate",
            when(
                col("cart_sessions") > 0,
                (
                    col("cart_sessions")
                    - col("order_sessions")
                )
                / col("cart_sessions"),
            ).otherwise(lit(0.0)),
        )
        .withColumn(
            "overall_conversion_rate",
            when(
                col("view_sessions") > 0,
                col("successful_payment_sessions")
                / col("view_sessions"),
            ).otherwise(lit(0.0)),
        )
    )


def build_product_performance(
    silver_df,
):

    orders = (
        silver_df
        .filter(
            col("event_type") == "ORDER"
        )
        .filter(
            col("order_id").isNotNull()
        )
        .filter(
            col("product_id").isNotNull()
        )
        .groupBy(
            "product_id"
        )
        .agg(
            countDistinct(
                "order_id"
            ).alias(
                "total_orders"
            ),
            sum(
                "quantity"
            ).alias(
                "units_sold"
            ),
            sum(
                "total_amount"
            ).alias(
                "gross_revenue"
            ),
            countDistinct(
                "customer_id"
            ).alias(
                "unique_customers"
            ),
        )
    )

    returns = (
        silver_df
        .filter(
            col("event_type") == "RETURN"
        )
        .filter(
            col("return_id").isNotNull()
        )
        .filter(
            col("product_id").isNotNull()
        )
        .groupBy(
            "product_id"
        )
        .agg(
            countDistinct(
                "order_id"
            ).alias(
                "returned_orders"
            ),
            sum(
                "refund_amount"
            ).alias(
                "refund_amount"
            ),
        )
    )

    return (
        orders
        .join(
            returns,
            on="product_id",
            how="left",
        )
        .fillna(
            {
                "returned_orders": 0,
                "refund_amount": 0.0,
            }
        )
        .withColumn(
            "return_rate",
            when(
                col("total_orders") > 0,
                col("returned_orders")
                / col("total_orders"),
            ).otherwise(
                lit(0.0)
            ),
        )
        .orderBy(
            col("gross_revenue").desc()
        )
    )


def main():

    spark = create_spark_session()

    spark.sparkContext.setLogLevel(
        "WARN"
    )

    silver_df = read_silver(
        spark
    )

    # -------------------------------
    # Daily Sales
    # -------------------------------

    daily_sales_df = build_daily_sales(
        silver_df
    )

    (
        daily_sales_df
        .write
        .mode("overwrite")
        .partitionBy(
            "sales_date"
        )
        .parquet(
            S3_GOLD_SALES_PATH
        )
    )

    print(
        "\n===== DAILY SALES ====="
    )

    daily_sales_df.show(
        truncate=False
    )

    # -------------------------------
    # Customer Funnel
    # -------------------------------

    funnel_df = build_customer_funnel(
        silver_df
    )

    (
        funnel_df
        .write
        .mode("overwrite")
        .parquet(
            S3_GOLD_FUNNEL_PATH
        )
    )

    print(
        "\n===== CUSTOMER FUNNEL ====="
    )

    funnel_df.show(
        truncate=False
    )

    # -------------------------------
    # Product Performance
    # -------------------------------

    product_df = build_product_performance(
        silver_df
    )

    (
        product_df
        .write
        .mode("overwrite")
        .parquet(
            S3_GOLD_PRODUCT_PATH
        )
    )

    print(
        "\n===== PRODUCT PERFORMANCE ====="
    )

    product_df.show(
        20,
        truncate=False
    )

    spark.stop()


if __name__ == "__main__":
    main()