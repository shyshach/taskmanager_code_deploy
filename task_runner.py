import simplejson as json
import boto3
import time


def run_task(event, context):
    body = event["body"]
    body = json.loads(body)
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('tasks')
    task_id = body.get("task_id")
    duration = body.get("duration")
    for i in range(int(duration)):
        if not table.get_item(Key={'task_id': task_id}).get("Item").get("status") == "cancelled":
            table.update_item(Key={'task_id': task_id},
                              UpdateExpression="SET #status = :g",
                              ExpressionAttributeValues={
                                  ':g': i+1
                              }, ExpressionAttributeNames={
                                "#status": "status"
                })
            time.sleep(1)
        else:
            return {
                'statusCode': 300,
                'body': task_id

            }
    return {
                'statusCode': 200,
                'body': task_id

            }