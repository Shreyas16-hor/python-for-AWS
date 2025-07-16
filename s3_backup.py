"""
This is a script to take a backup from local to AWS S3
boto3 is library used to do AWS tasks using python
"""
import boto3

s3 = boto3.resource("s3")
def show_bucketes(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)
    
def create_bucket(s3,bucket_name,region):
    s3.create_bucket(Bucket="python-forr-cloud", CreateBucketConfiguration={
        'LocationConstraint':'us-east-2',
    },)
    print("Bucket created successfully")

def upload_backup(s3, file_name, bucket_name, key_name): 
    with open(file_name, 'rb') as data:
        s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
    print("✅ Backup uploaded successfully")



bucket_name ="python-forr-cloud"
region = "us-east-2"      
# create_bucket(s3,bucket_name,region)    
# show_bucketes(s3) 
file_name = "C:\\Users\\shreyas\\p\\backups\\backup_2025-07-15.tar.gz"  
upload_backup(s3,file_name,bucket_name,"my-backup.tar.gz") 



