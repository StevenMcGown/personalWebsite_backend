import boto3
import json
from botocore.session import Session
from botocore.config import Config

s = Session()
c = s.create_client('s3', config=Config(connect_timeout=5, read_timeout=60, retries={'max_attempts': 2}))

def lambda_test(event, context):
    '''
    Retrieving the initial value of the visitor count
    '''
    dynamoDB_client = boto3.client('dynamodb')

    initial_value = dynamoDB_client.get_item(
        TableName='counter',
        Key={
            'page_name' : {'S': 'resume'},
        }
    )
    initial_value = int(initial_value['Item']['count']['N'])

    '''
    This portion of the test invokes the increment
    lambda function and then returns the payload. The visitor
    count is extracted and then compared with the previous number.
    If the function runs correctly, the value should be one more
    than the original value.
    '''
    lambda_client = boto3.client('lambda')

    invoke_response = lambda_client.invoke(
        FunctionName=
        "visitor-counter-HelloWorldFunction-6hE6IdBQgEGA"
    )
    # Loads the payload from the reponse of the counter lambda function
    data = json.loads(invoke_response['Payload'].read())

    # Probably not the most efficient or elegant way but it works
    data = json.loads(data['body'])
    incremented_value = int(data['Visitors'])

    # Will 1 more than initial value
    assert(initial_value + 1 == incremented_value)

    '''
    The original value should be re-instated but only if the
    assertion passed
    '''
    dynamoDB_client.put_item(
        TableName='counter',
        Item={
            'page_name' : {'S': 'resume'},
            'count' : {'N': str(initial_value)}
        }
    )
    print("ok")