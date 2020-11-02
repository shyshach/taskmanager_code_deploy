import json
import boto3


def login(event, context):
    body = event["body"]
    body = json.loads(body)
    password = body["password"]
    username = body["username"]
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')
    item = table.get_item(Key={"username": username}).get("Item")
    if not item:
        return {
            'statusCode': 400,
            'body': "Invalid username"
        }

    if username == item.get("username"):
        return {
            'statusCode': 200,
            'body': item["password"]
        }
    else:
        return {
            'statusCode': 400,
            'body': "Invalid password or username"
        }
