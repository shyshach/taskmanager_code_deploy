import json
import boto3


def stop_task(event, context):
    body = event["body"]
    body = json.loads(body)
    task_id = body["task_id"]
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('tasks')
    item = table.get_item(Key={'task_id': task_id}).get("Item")
    if item and str(item["duration"]) != str(item["status"]):
        table.update_item(Key={'task_id': task_id},
                          UpdateExpression="SET #status = :g",
                          ExpressionAttributeValues={
                            ':g': "cancelled"
                        }, ExpressionAttributeNames={
                                "#status": "status"
                        })
        return {
            'statusCode': 200,
            'body': "Stopped"
        }
    else:
        return {
                'statusCode': 400,
                'body': "No such task or task ended already"
            }

