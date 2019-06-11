
import boto3
dynamoDb = boto3.resource('dynamodb')
table_name = dynamoDb.Table ('Game-AA')


response1 = table_name.get_item(
    Key= {
        'Gid': 1
    }
)
item=response1['Item']
print('gname=',item['gname'],
      'rating=',item['rating'])


######query
#response = table_name.query(
#    KeyConditionExpression=Key('Gid').eq('1')
#)
#item2=response['Item']
#print('gname=' , response[0]['gname'] ,
#      'rating=' , response[0]['rating']
      )