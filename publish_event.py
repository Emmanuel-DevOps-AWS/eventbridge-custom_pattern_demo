import json
import boto3
import datetime

client = boto3.client('events')

def lambda_handler(event, context):
    
    response = client.put_events(
        Entries=[
            {
            'Time': datetime.datetime.now(),
            'Source': 'Lambda Publish',
            'Resources': [
             ],
            'DetailType': 'Custom event demo',
            'Detail': json.dumps(event),
            'EventBusName': 'INSERT EVENT BUS ARN',
            'TraceHeader': 'testdemo'
             },
                ]
             )
    return response