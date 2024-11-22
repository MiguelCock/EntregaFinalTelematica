from pyspark.sql import SparkSession
import requests
import sys

FILENAME = "covid_data.csv"

if __name__ == "__main__":
    url = "https://www.datos.gov.co/api/views/gt2j-8ykr/rows.csv?fourfour=gt2j-8ykr&cacheBust=1723672007&date=20241121&accessType=DOWNLOAD"
    response = requests.get(url)
    if response.status_code == 200:
        with open(FILENAME, "wb") as file:
            file.write(response.content)
        print(f"File downloaded successfully: {FILENAME}")

        spark = SparkSession.builder.appName("SaveFileToS3").getOrCreate()
        df = spark.read.csv(FILENAME, header=True, inferSchema=True)
        df.write.mode("overwrite").csv(sys.argv[1])
    else:
        print(f"Failed to download file. HTTP Status Code: {response.status_code}")