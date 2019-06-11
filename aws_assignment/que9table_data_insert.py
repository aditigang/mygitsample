import boto3
dynamoDb = boto3.resource('dynamodb')
print("Name of table in which data is to be added")
table_name = dynamoDb.Table (input(""))
print(table_name.name)

Item = {
        'Gid': 1,
        'gname': "Mario",
        'publisher': "Mario Inc.",
        'rating': 9,
        'release_date': "09-01-1997",
        'genres': ["G1", "G2"]
        }


resource= table.put_item(Item=Item)
print("done")