import boto3 

s3 = boto3.resource('s3')

my_bucket = s3.Bucket('11am-devops')

for i in my_bucket.objects.all():
    print(i.key)