import json
import os
import boto3

def lambda_handler(event, context):
    # TODO implement
    sagemaker = boto3.client('sagemaker')
    try:
        name = 'decision-tree-endpoint-000'
        image = '{account-id}.dkr.{region}.amazonaws.com/decision-tree:latest'
        model_data_url = 's3://customized-sagemaker-image-decision-tree-bucket/input/model/model.tar.gz'
        execution_role_arn = 'arn:aws:iam::{account-id}:role/create-decision-tree-sagemaker-endpoint-role'
        instance_count = 1
        instance_type = 'ml.m5.large'
        
        model_name = name
        endpoint_config_name = name
        inference_endpoint_name = name
        
        
        
        response = sagemaker.create_model(
            ModelName=model_name,
            PrimaryContainer={
                'Image': image,
                'ModelDataUrl': model_data_url
            },
            ExecutionRoleArn=execution_role_arn,
        )
        
        response = sagemaker.create_endpoint_config(
            EndpointConfigName=endpoint_config_name,
            ProductionVariants=[
                {
                    'VariantName': 'AllTraffic',
                    'ModelName': model_name,
                    'InitialInstanceCount': instance_count,
                    'InstanceType': instance_type,
                },
            ],
        )
        
        response = sagemaker.create_endpoint(
            EndpointName=inference_endpoint_name,
            EndpointConfigName=endpoint_config_name,
        )
        
        print('[INFO] CREATE SUSSESSFULLY!')
        print(response)
        
        return {
            'status': 'Success',
        }
    
    except Exception as e:
        print('[INFO] FAIL TO CREATE ENDPOINT!')
        print(e)
        return {
            'status': 'Error'
        }
