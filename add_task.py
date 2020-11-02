import json
import boto3


def add_task(event, context):
    body = event["body"]
    body = json.loads(body)

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('tasks')
    lambdae = boto3.client("lambda")
    if body.get("username") and body.get("duration"):
        table.put_item(
        Item={
            'task_id': context.aws_request_id,
            'author_username': body["username"],
            "status": 0,
            "duration": int(body["duration"])
        }
        )
        invoke_response = lambdae.invoke(FunctionName="taskmanager-dev-run_task",
                                     InvocationType='Event',
                                     Payload=json.dumps({
                                         "task_id": context.aws_request_id,
                                         "duration": int(body["duration"])
                                     }))
        print(invoke_response)
        return {
        'statusCode': 200,
        'body': context.aws_request_id

        }
    else:
        return {
        'statusCode': 400,
        'body': "Bad body"
        }
