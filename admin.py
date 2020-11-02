import simplejson as json
import boto3


def admin(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('tasks')
    response = table.scan().get("Items")
    return {
        "statusCode": 200,
        "body": json.dumps(response)}

