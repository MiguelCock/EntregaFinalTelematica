CREATE EXTERNAL TABLE IF NOT EXISTS `covid`.`b` (`departamento_nom` string, `count` int)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION 's3://bucketjonathanretos/trusted/api'
TBLPROPERTIES ('classification' = 'parquet');