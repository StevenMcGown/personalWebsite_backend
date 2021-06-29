import json
import boto3
# import requests


def lambda_handler(event, context):
    client = boto3.client('dynamodb')

    count = client.get_item(
        TableName='counter',
        Key={
            'page_name' : {'S': 'resume'},
        }
    )

    count = str(int(count['Item']['count']['N']) + 1)

    response = client.put_item(
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

def lambda_test(event, context):
    client = boto3.client('dynamodb')
    
    #getting initial value
    test_count_before_put = client.get_item(
        TableName='counter',
        Key = {
            'page_name' : {'S': 'resume'},
        }
    )
    #increment the count
    test_count = str(int(test_count_before_put['Item']['count']['N']) + 1)

    #putting incremented value
    client.put_item(
        TableName='counter',
        Item = {
           'page_name' : {'S': 'resume'},
           'count' : {'N': test_count}
        }
    )

    #getting new value from dynamo
    test_count_after_put = client.get_item(
        TableName='counter',
        Key = {
            'page_name' : {'S': 'resume'},
        }
    )
    #test case
    assert(int(test_count_before_put['Item']['count']['N']) + 1
        == int(test_count_after_put['Item']['count']['N'])), 'Incremented incorrectly'
    
    #changing original value to string value of indexed integer
    test_count_before_put = str(int(test_count_before_put['Item']['count']['N']))

    #put the original value before testing
    client.put_item(
        TableName='counter',
        Item = {
           'page_name' : {'S': 'resume'},
           'count' : {'N': test_count_before_put}
        }
    )