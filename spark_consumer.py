from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StringType, IntegerType
from pyspark.sql.types import *
def Spark_cons():
    spark = SparkSession.builder \
        .appName("KafkaSparkPipeline") \
        .config("spark.jars.packages",
            "org.apache.spark:spark-sql-kafka-0-10_2.13:4.1.1,"
            "mysql:mysql-connector-java:8.0.33") \
        .getOrCreate()

    schema = StructType() \
        .add("event", StringType()) \
        .add("Busname",StringType()) \
        .add("Bustype",StringType()) \
        .add("Departure",StringType()) \
        .add("Duration",StringType()) \
        .add("Arrival",StringType()) \
        .add( "Seats_Avail",StringType()) \
        .add("Price",StringType()) \
        .add("Star_Rate",StringType()) \
        .add("request_id", StringType())
    kafka_df = spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("startingOffsets", "earliest") \
        .option("subscribe", "bus_topic") \
        .load()

    json_df = kafka_df.selectExpr("CAST(value AS STRING)")

    parsed_df = json_df.select(
        from_json(col("value"), schema).alias("data")
    ).select("data.*")

    def write_to_mysql(batch_df, batch_id):
        print("🔥 Writing batch:", batch_id)
        print("Row count:", batch_df.count())
        batch_df.write \
            .format("jdbc") \
            .option("url", "jdbc:mysql://localhost:3306/now") \
            .option("driver", "com.mysql.cj.jdbc.Driver") \
            .option("dbtable", "redbus_table") \
            .option("user","root") \
            .option("password", "Ramk@2001") \
            .mode("append") \
            .save()

    query = parsed_df.writeStream \
        .foreachBatch(write_to_mysql) \
        .outputMode("append") \
        .start()
    

    query.awaitTermination()
