import json


def lambda_handler(event, context):
    print(event)
    s = event['queryStringParameters']['name']
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! ' + str(s))
    }
