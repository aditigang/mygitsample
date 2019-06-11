import json
import boto3
import pymysql
from datetime import datetime


def lambda_handler(event, context):
    rds_host = "aditi.csaruqlxxway.us-east-1.rds.amazonaws.com"
    name = "aditi"
    password = "aditi999"
    db_name = "aditi"
    connection = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    cursor = connection.cursor()

    client = boto3.client('dynamodb')
    response = client.scan(
        TableName='DynamoAG',
        Limit=123,
        Select='ALL_ATTRIBUTES'
    )
    create_table_query = """create table Citizendata(
                ID int auto_increment primary key,
                Gender varchar(1) not null,
                Date varchar(10) not null
                )"""
    # cursor.execute(create_table_query)

    for i in response['Items']:
        element_ID = i['ID']['N']
        date = i['Date']['S']
        gen = i['Gender']['S']
        if gen == 'm':
            element_gender = 'Male'
        else:
            element_gender = 'Female'

        d = datetime.strptime(date, "%d/%m/%y")
        element_date = datetime.strftime(d, '%d-%m-%Y')

        # inserting data into table

        cursor.execute(""" insert into Citizendata (ID,Gender,Date) values(%s,'%s','%s')""" % (
        element_ID, element_gender, element_date))
        cursor.execute(""" select * from Citizendata""")
        connection.commit()

    connection.close()
    print("its done!!!")

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }