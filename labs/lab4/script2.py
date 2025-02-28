import boto3
import requests
import sys

# number of arguments 
if len(sys.argv) != 4:
    print("Usage: python script2.py <file_url> <bucket_name> <expiration_time>")
    sys.exit(1)

file_url = sys.argv[1]
bucket_name = sys.argv[2]
expiration_time = int(sys.argv[3])

# Download file from URL
file_name = file_url.split("/")[-1]
response = requests.get(file_url)
with open(file_name, "wb") as file:
    file.write(response.content)

print(f"Downloaded {file_name}")

# Connect
s3 = boto3.client("s3")

# Upload file 
s3.upload_file(file_name, bucket_name, file_name)
print(f"Uploaded {file_name} to {bucket_name}")

# Generate presigned URL
presigned_url = s3.generate_presigned_url(
    "get_object",
    Params={"Bucket": bucket_name, "Key": file_name},
    ExpiresIn=expiration_time,
)

print(f"Presigned URL (valid for {expiration_time} seconds): {presigned_url}")
