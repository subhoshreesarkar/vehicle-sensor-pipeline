import boto3
import os
from dotenv import load_dotenv

# Load AWS credentials from .env file
load_dotenv()

def upload_to_s3(local_file, bucket_name, s3_filename):
    """
    Uploads a local file to an AWS S3 bucket.
    """
    # Create S3 client with credentials from environment variables
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION")
    )

    try:
        s3_client.upload_file(local_file, bucket_name, s3_filename)
        print(f"✅ File '{local_file}' successfully uploaded to S3 bucket '{bucket_name}'!")
    except Exception as e:
        print(f"❌ Upload failed: {e}")

if __name__ == "__main__":
    upload_to_s3(
        local_file="sensor_data_raw.csv",
        bucket_name="vehicle-sensor-pipeline-tobias",
        s3_filename="raw/sensor_data_raw.csv"
    )
