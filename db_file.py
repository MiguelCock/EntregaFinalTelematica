from pyspark.sql import SparkSession

BUCKET_NAME = "bucketjonathanretos"
RAW_FOLDER = "raw/"
TRUSTED_FOLDER = "trusted/"
RAW_FILENAME = "covid_data.csv"
TRUSTED_FILENAME = "covid_analysis.parquet"

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("Covid Data Analysis") \
        .getOrCreate()

    raw_data_path = f"s3a://{BUCKET_NAME}/{RAW_FOLDER}{RAW_FILENAME}"
    raw_data = spark.read.csv(raw_data_path, header=True, inferSchema=True)

    analysis = raw_data.groupBy("Departamento o Distrito").count()

    trusted_data_path = f"s3a://{BUCKET_NAME}/{TRUSTED_FOLDER}{TRUSTED_FILENAME}"
    analysis.write.mode("overwrite").parquet(trusted_data_path)

    print(f"Analysis saved to: {trusted_data_path}")
