import os
import io
import boto3
import json
import csv

runtime= boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    # TODO implement

    response = runtime.invoke_endpoint(EndpointName='decision-tree-endpoint-000',
                                      ContentType='text/csv',
                                      Body='1,2,3,4')
    response_body = response['Body'].read().decode('utf-8')
    print(response_body)
    preds = {"Prediction": response_body}
    print(preds)
    response_dict = {
          "statusCode": 200,
          "body": json.dumps(preds)
                }
    return response_dict