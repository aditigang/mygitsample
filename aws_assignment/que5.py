import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('source-aditi')
    copy_bucket = 'destination-aditi'

    for obj in bucket.objects.all():
        copy_source = {
            'Bucket': 'source-aditi',
            'Key': obj.key
        }
        s3.meta.client.copy(copy_source, 'destination-aditi', obj.key)
    print("objects copied")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
