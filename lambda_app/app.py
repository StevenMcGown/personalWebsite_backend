import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('dynamodb')
    count = client.get_item(
        TableName='counter',
        Key={
            'page_name' : {'S': 'resume'},
        }
    )

    count = str(int(count['Item']['count']['N']) + 1)

    client.put_item(
            TableName='counter',
            Item={
                'page_name' : {'S': 'resume'},
                'count' : {'N': count}
            }
    )

    return {
        "statusCode": 200,
        'headers': {
            "Access-Control-Allow-Origin": "*",
        },
        "body": json.dumps({
            "Visitors": count,
        }),
    }
