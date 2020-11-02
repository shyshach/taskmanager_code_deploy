import simplejson as json
import boto3
from boto3.dynamodb.conditions import Key, Attr



def list_tasks(event, context):
    body = event["body"]
    body = json.loads(body)
    username = body["username"]
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('tasks')
    response = table.scan(FilterExpression=Attr("author_username").eq(username)).get("Items")
    return {
        "statusCode": 200,
        "body": json.dumps(response)}

