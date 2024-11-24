from pyspark.sql import SparkSession
import sys

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("Covid Data Analysis") \
        .getOrCreate()

    raw_data = spark.read.csv(sys.argv[1], header=True, inferSchema=True)

    analysis = raw_data.groupBy("ciudad_municipio").count()

    print(analysis.show())

    analysis.write.mode("overwrite").parquet(sys.argv[2])

    spark.stop()