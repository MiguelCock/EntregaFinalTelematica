import requests
import sys
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("Covid Data Analysis from API") \
        .getOrCreate()

    api_url = "https://www.datos.gov.co/resource/gt2j-8ykr.json"
    response = requests.get(api_url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from API. HTTP Status Code: {response.status_code}")

    data = response.json()

    if len(data) == 0:
        raise Exception("No data returned from the API.")

    sample_record = data[0]
    schema = StructType([
        StructField(key, StringType(), True) for key in sample_record.keys()
    ])

    normalized_data = [
        {key: record.get(key, None) for key in sample_record.keys()} for record in data
    ]

    rdd = spark.sparkContext.parallelize(normalized_data)

    df = spark.createDataFrame(rdd, schema=schema)

    analysis = df.groupBy("departamento_nom").count()
    analysis.show()

    analysis.write.mode("overwrite").parquet(sys.argv[1])

    spark.stop()
