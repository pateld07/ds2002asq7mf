#!/bin/bash


if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <local_file> <bucket_name> <expiration_time>"
    exit 1
fi

# Assign 
LOCAL_FILE=$1
BUCKET_NAME=$2
EXPIRATION=$3

# Upload file 
aws s3 cp "$LOCAL_FILE" s3://"$BUCKET_NAME"/


PRESIGNED_URL=$(aws s3 presign --expires-in "$EXPIRATION" s3://"$BUCKET_NAME"/"$LOCAL_FILE")

# Output the URL
echo "Presigned URL (valid for $EXPIRATION seconds):"
echo "$PRESIGNED_URL"
