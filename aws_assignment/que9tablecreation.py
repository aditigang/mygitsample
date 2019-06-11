from __future__ import print_function
import os
import botocore.session

region = os.environ.get('AWS_DEFAULT_REGION', 'us-east-1')
session = botocore.session.get_session()
dynamodb = session.create_client('dynamodb', region_name=region) # low-level client

print("Name of the table to be created:")
table_name = input("")

params = {
    'TableName' : table_name,
    'KeySchema': [ { 'AttributeName': "Gid", 'KeyType': "HASH"} ],  # Partition key

    'AttributeDefinitions': [  { 'AttributeName': "Gid", 'AttributeType': "N" }  ],

    'ProvisionedThroughput': {
                        'ReadCapacityUnits': 10,
                        'WriteCapacityUnits': 10
                         }
        }
dynamodb.create_table(**params)

print('Waiting for', table_name, '...')
waiter = dynamodb.get_waiter('table_exists')
waiter.wait(TableName=table_name)
