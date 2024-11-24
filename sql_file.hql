CREATE DATABASE IF NOT EXISTS covid_db;
USE covid_db;

CREATE EXTERNAL TABLE IF NOT EXISTS covid_data (
    fecha_reporte_web STRING,
    id_de_caso STRING,
    fecha_de_notificacion STRING,
    departamento STRING,
    departamento_nom STRING,
    ciudad_municipio STRING,
    ciudad_municipio_nom STRING,
    edad INT,
    unidad_medida STRING,
    sexo STRING,
    fuente_tipo_contagio STRING,
    ubicacion STRING,
    estado STRING,
    pais_viajo_1_cod STRING,
    pais_viajo_1_nom STRING,
    recuperado STRING,
    fecha_inicio_sintomas STRING,
    fecha_muerte STRING,
    fecha_diagnostico STRING,
    fecha_recuperado STRING,
    tipo_recuperacion STRING,
    per_etn STRING,
    nom_grupo STRING
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION 's3://bucketjonathanretos/raw/';