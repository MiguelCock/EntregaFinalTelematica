import requests
import boto3
import os

BUCKET_NAME = "bucketjonathanretos"
RAW_FOLDER = "raw/"
FILENAME = "covid_data.csv"

def download_csv(url, local_file):
    response = requests.get(url)
    if response.status_code == 200:
        with open(local_file, "wb") as file:
            file.write(response.content)
        print(f"File downloaded successfully: {local_file}")
    else:
        print(f"Failed to download file. HTTP Status Code: {response.status_code}")

def upload_to_s3(local_file, s3_bucket, s3_key):
    s3 = boto3.client("s3")
    s3.upload_file(local_file, s3_bucket, s3_key)
    print(f"File uploaded to S3: s3://{s3_bucket}/{s3_key}")

if __name__ == "__main__":
    url = "https://www.datos.gov.co/api/views/gt2j-8ykr/rows.csv?fourfour=gt2j-8ykr&cacheBust=1723672007&date=20241121&accessType=DOWNLOAD"
    local_file = FILENAME
    s3_key = f"{RAW_FOLDER}{FILENAME}"

    download_csv(url, local_file)

    upload_to_s3(local_file, BUCKET_NAME, s3_key)

    os.remove(local_file)
