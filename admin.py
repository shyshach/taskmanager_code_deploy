import simplejson as json
import boto3


def admin(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('tasks')
    response = table.scan().get("Items")
    client = boto3.client("lambda")
    response2 = client.get_function(
        FunctionName='taskmanager-dev-run_task')
    dc = {
        "tasks": response,
        "lambda": response2

    }
    return {
        "statusCode": 200,
        "body": json.dumps(dc)

    }

