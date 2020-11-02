import json
import boto3


def create_user(event, context):
    body = event["body"]
    body = json.loads(body)

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')
    if table.get_item(Key={'username': body["username"]}).get("Item"):
        return {
            'statusCode': 400,
            'body': "User with that name already exists."
        }
    else:
        table.put_item(
            Item={
                'username': body["username"],
                'password': str(body["password"]),
                'email': str(body["email"])
            }
        )
    return {
        'statusCode': 200,
        'body': f"User {body['username']} created"

    }
