# import json
# import boto3

# def lambda_handler(file_name, bucket, object_name=None):
    
#     file_name= "NEWONE"
#     bucket= "targetbucket-moabdou"

#     # If S3 object_name was not specified, use file_name
#     if object_name is None:
#         object_name = file_name

#     # Upload the file
#     boto3.client('s3').upload_file(file_name, bucket, object_name)
