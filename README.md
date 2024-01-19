# eventbridge-custom_pattern_demo

Make sure to attach the appropriate role to the publish lambda function

Steps
- Create a 2 lambda functions
    - Insert the publish_event.py code into the first function 
        - make sure this Lambda function has permission to publish to eventbridge
    - Insert the read_event.py code into the secnd function
        - make sure this Lambda function has CloudWatch permission
- Create an event bus
- Create a rule for the newly created eventbus
    - For the custom rule pattern, paste the content of the "custom_rule.json" file
    - Specify that the target should be a Lambda Function and select you read_event Lambda function as the target
    - Review and create your rule
- Navigate to the publish_event Lambda function and create 2 test
    - paste the content of Event_test_A and Event_test_B respectively and save
- Run a test on the publish_event lambda function 
- Navigate to the read_event Lambda function, move to the the monitor tab and select 'view cloudwatch log'
    - select the latest Log Stream and you should have a log entry that looks like this;
    {'version': '0', 'id': '1e85971f-cee3-b4d1-9f8f-fb1fjfxaa4c62a', 'detail-type': 'Custom event demo', 'source': 'Lambda Publish', 'account': 'xxxxxxxxxxxx', 'time': '20xx-xx-19T16:00:05Z', 'region': 'us-east-1', 'resources': [], 'detail': {'name': 'sarah', 'salary': '6875', 'married': 'true'}}
- if you don't have this log entry, wait for a few minute, you might be having some latency
- if the log entry still doesn't exist, read through the steps again to see where you might have made a mistake and start troubleshooting
