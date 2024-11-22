#!/bin/bash

CSV_URL="https://www.datos.gov.co/resource/gt2j-8ykr.csv"

S3_BUCKET="s3://bucketjonathanretos/raw"
FILENAME="covid_data.csv"

wget -O /tmp/$FILENAME $CSV_URL
if [ $? -ne 0 ]; then
    echo "Failed to download the CSV file from $CSV_URL"
    exit 1
fi

aws s3 cp /tmp/$FILENAME $S3_BUCKET/$FILENAME
if [ $? -ne 0 ]; then
    echo "Failed to upload the file to $S3_BUCKET/$FILENAME"
    exit 1
fi

echo "File successfully downloaded and uploaded to $S3_BUCKET/$FILENAME"
