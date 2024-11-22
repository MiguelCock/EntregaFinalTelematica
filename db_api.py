import requests
from pyspark.sql import SparkSession

TRUSTED_BUCKET_NAME = "bucketjonathanretos"
TRUSTED_FOLDER = "trusted/"
TRUSTED_FILENAME = "covid_analysis_from_api.parquet"

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("Covid Data Analysis from API") \
        .getOrCreate()

    api_url = "https://www.datos.gov.co/resource/gt2j-8ykr.json"
    response = requests.get(api_url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from API. HTTP Status Code: {response.status_code}")

    data = response.json()
    rdd = spark.sparkContext.parallelize(data)

    columns = ["fecha reporte web", "id_de_caso", "fecha_de_notificaci_n", "departamento", "departamento_nom", "ciudad_municipio", "ciudad_municipio_nom", "edad", "unidad_medida", "sexo", "fuente_tipo_contagio", "ubicacion", "estado", "pais_viajo_1_cod", "pais_viajo_1_nom", "recuperado", "fecha_inicio_sintomas", "fecha_muerte", "fecha_diagnostico", "fecha_recuperado", "tipo_recuperacion", "per_etn_", "nom_grupo_",]
    df = spark.createDataFrame(rdd, schema=columns)

    analysis = df.groupBy("departamento").count()

    trusted_data_path = f"s3a://{TRUSTED_BUCKET_NAME}/{TRUSTED_FOLDER}{TRUSTED_FILENAME}"
    analysis.write.mode("overwrite").parquet(trusted_data_path)

    print(f"Analysis saved to: {trusted_data_path}")